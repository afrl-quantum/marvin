# vim: et:sw=2:ts=2:nowrap

from ctypes import Structure, c_uint32
import numpy as np

__all__ = ['ReconfigRegister', 'Reconfig']

def mask32(width, MAX_BITS=32):
  """
  make a mask of the lowest [width] bits of a [MAX_BITS] bit vector.
  """
  ones = ~(~0 << 32)
  return ones >> ( MAX_BITS - width )

class Dict(dict):
  def __init__(self,*a,**kw):
    super(Dict, self).__init__(*a,**kw)
    self.__dict__ = self

class ReconfigRegister(c_uint32):
  """
  the layout of the reconfig register:
    register[2..0] : command ('read', 'write', 'reconfig', 'reset', 'pll_reset')
    register[6..3] : COUNTER ('c0','c1',...,'cp_lf','vco','m','n')
    register[9..7] : parameter name (
          for c0..c4: 'high_count', 'low_count', 'bypass', 'mode',
          for m,n   : 'high_count', 'low_count', 'bypass', 'mode','nominal'
          for vco   : 'post_scale',
      )
    register[18..10]: parameter data
    register[31..19]: unused
          
  """

  def __init__(self, *a,**kw):
    super(ReconfigRegister,self).__init__(*a)
    for k,v in kw.items():
      if k not in FORWARD:
        raise LookupError('uknown bit value: "{}"'.format(k))
        self.set_item(k,v)

  BIT0    = dict()
  WIDTH   = dict()
  FORWARD = dict()
  REVERSE = dict()

  #union with status: valid only on writes
  BIT0['CMD']   = 0
  WIDTH['CMD']  = 3
  FORWARD['CMD'] = dict(
    noop        = 0b000, # 0
    read        = 0b001, # 1
    write       = 0b010, # 2
    reconfig    = 0b011, # 3
    reset       = 0b100, # 4
    pll_reset   = 0b101, # 5
    clk_switch  = 0b110, # 6
  )
  REVERSE['CMD'] = { 0:{v:k for k,v in FORWARD['CMD'].viewitems()} }

  #union with cmd: valid only on reads
  BIT0['LOCKED']   = 0
  WIDTH['LOCKED']  = 1
  BIT0['BUSY']   = 1
  WIDTH['BUSY']  = 1


  BIT0['COUNTER'] = 3
  WIDTH['COUNTER'] = 4
  FORWARD['COUNTER'] = dict(
    n       = 0b0000,
    m       = 0b0001,
    cp_lf   = 0b0010,
    vco     = 0b0011,
    c0      = 0b0100,
    c1      = 0b0101,
    c2      = 0b0110,
    c3      = 0b0111,
    # these don't seem to exist for our device:
    #c4      = 0b1000,
    #c5      = 0b1001,
    #c6      = 0b1010,
    #c7      = 0b1011,
    #c8      = 0b1100,
    #c9      = 0b1101,
  )
  REVERSE['COUNTER'] = { 0:{v:k for k,v in FORWARD['COUNTER'].viewitems()} }

  BIT0['PARAM'] = 7
  WIDTH['PARAM'] = 3
  FORWARD['PARAM'] = dict(
    cp_lf = dict(
      # for charge pump / loop filter
      cp_unused   = 0b101,
      cp_current  = 0b000,
      lf_unused   = 0b100,
      lf_resistor = 0b001,
      lf_capacitor= 0b010,
    ),

    # for vco
    vco = dict(
      vco_post_scale = 0b000,
    ),

    **{
      c:dict(
        # for counters
        high_count  = 0b000,
        low_count   = 0b001,
        bypass      = 0b100,
        odd         = 0b101,
        nominal     = 0b111,
      ) for c in ['m','n','c0','c1','c2','c3','c4','c5','c6','c7','c8','c9']
    }
  )
  REVERSE['PARAM'] = { k0:{v:k for k,v in D.viewitems()}
    for k0,D in FORWARD['PARAM'].viewitems()
  }
  FORWARD['PARAM'] = reduce( lambda D,d : dict(D,**d),
                             [dict()] + FORWARD['PARAM'].values() )

  BIT0['DATA'] = 10
  WIDTH['DATA'] = 9

  # just change WIDTH to get a wider selection
  BIT0['inclk'] = 19
  WIDTH['inclk'] = 1
  FORWARD['inclk'] = {
    '80' : 0b0, #MHz
    '10' : 0b1, #MHz
  }
  REVERSE['inclk'] = { 0:{v:k for k,v in FORWARD['inclk'].viewitems()} }


  def get_item(self,name,sub):
    """
    Retrieve the value of a subset of bits.
    """
    b0 = self.BIT0[name]
    msk = mask32( self.WIDTH[name] )
    return self.REVERSE[name][sub][ (self.value >> b0) & msk ]
  def set_item(self, name, value):
    """
    Set the value of a subset of bits.
    """
    if type(value) is str:
      value = self.FORWARD[name][ value.lower() ]
    else:
      assert value in self.FORWARD[name].values()
    b0 = self.BIT0[name]
    msk = mask32( self.WIDTH[name] )
    self.value = (self.value & ~(msk<<b0)) | (value << b0)



  @property
  def cmd(self):
    return self.get_item('CMD',0)
  @cmd.setter
  def cmd(self, value):
    self.set_item('CMD', value)

  @property
  def counter(self):
    return self.get_item('COUNTER',0)
  @counter.setter
  def counter(self, counter):
    return self.set_item('COUNTER', counter)

  @property
  def param(self):
    return self.get_item('PARAM',self.counter)
  @param.setter
  def param(self, parameter_name):
    return self.set_item('PARAM', parameter_name)

  @property
  def data(self):
    b0 = self.BIT0['DATA']
    msk = mask32( self.WIDTH['DATA'] )
    return (self.value >> b0) & msk
  @data.setter
  def data(self, data):
    b0 = self.BIT0['DATA']
    msk = mask32( self.WIDTH['DATA'] )
    self.value = (self.value & ~(msk<<b0)) | (data << b0)

  @property
  def inclk(self):
    return int( self.get_item('inclk',0) )
  @inclk.setter
  def inclk(self, inclk_i):
    return self.set_item('inclk', str(inclk_i))

  @property
  def locked(self):
    return self.value & 0x1

  @property
  def busy(self):
    return (self.value >>1 ) & 0x1


  def __repr__(self):
    return 'ReconfigRegister(' \
           '  counter={counter},' \
           '  param={param},' \
           '  data ={data},' \
           '  cmd={cmd}' \
           ')'.format(
      cmd = self.cmd,
      counter = self.counter,
      param = self.param,
      data = self.data,
    )


class Reconfig(object):
  def __init__( self, fpga, write_address, read_address=None, addr_space='reg',
                Fin=None, output_counters=['c0'] ):
    self.fpga = fpga
    self.write_address = write_address
    self.read_address = write_address if read_address is None else read_address
    self.addr_space = addr_space
    self.reg = ReconfigRegister()
    self.output_counters = output_counters
    self._Fin = None
    self.Fin = Fin
    self.Fvco_extrema = xrange(600, 1201)

  def _set(self, counter, param, value, reconfig=False):
    self.reg.cmd = 'write'
    self.reg.counter = counter
    self.reg.param = param
    self.reg.data = value

    # now write this to the fpga
    self.fpga.write(self.addr_space, self.write_address, self.reg)
    if reconfig:
      self.reconfig()

  def set(self, counter, reconfig=False, **params):
    for P,V in params.items():
      self._set( counter, P, V )
    if reconfig:
      self.reconfig()


  def get(self, counter, param):
    self.reg.cmd = 'read'
    self.reg.counter = counter
    self.reg.param = param

    # now write this to the fpga
    self.fpga.write(self.addr_space, self.write_address, self.reg)
    # get response from fpga
    reg = ReconfigRegister( self.fpga.read(self.addr_space, self.read_address) )
    return reg.data

  @property
  def status(self):
    reg = ReconfigRegister( self.fpga.read(self.addr_space, self.read_address) )
    return Dict(
      locked = bool(reg.locked),
      busy = bool(reg.busy),
      inclk = reg.inclk,
    )

  def reconfig(self):
    self.reg.cmd = 'reconfig'
    self.fpga.write(self.addr_space, self.write_address, self.reg)

  @property
  def frequencies(self):
    M = 1 if self.get('M','bypass') else self.get('M','high_count') + self.get('M','low_count')
    N = 1 if self.get('N','bypass') else  self.get('N','high_count') + self.get('N','low_count')

    C = {
      c:(1 if self.get(c,'bypass') else self.get(c,'high_count') + self.get(c,'low_count'))
      for c in self.output_counters
    }

    vco  = self.Fin * (M/N)
    return dict(
      Fin   = self.Fin,
      vco  = vco,
      **{ c: vco / Ci for c,Ci in C.items() }
    )


  @property
  def Fin(self):
    return self._Fin

  @Fin.setter
  def Fin(self, value, reconfig=True):
    if self._Fin is not None:
      F = self.frequencies
      #M_N_0 = F['vco'] / self._Fin
      #M_N_1 = F['vco'] / value
      if F['vco'] != 600:
        raise NotImplementedError('Expecting F_vco == 600 MHz!')


    if value not in self.F_param:
      raise NotImplementedError('need to figure out arbitrary frequency control...')
    for counter,params in self.F_param[value].items():
      self.set( counter, **params )
    self._Fin = value

    if reconfig:
      self.set_inclk( value )
      self.reconfig()

  def set_inclk(self, value):
    self.reg.cmd = 'clk_switch'
    self.reg.inclk = value
    self.fpga.write(self.addr_space, self.write_address, self.reg)


  # a cheat until we figure this out completely
  F_param = {
    10: dict(
      M = dict(bypass=0,high_count=30,low_count=30,odd=0),
      N = dict(bypass=1,high_count=0,low_count=0,odd=0),
      cp_lf = dict(lf_resistor=19, lf_capacitor=0),
      vco = dict( vco_post_scale = 0 ),
    ),

    80: dict(
      M = dict(bypass=0,high_count=8,low_count=7,odd=1),
      N = dict(bypass=1,high_count=1,low_count=0,odd=0),
      cp_lf = dict(lf_resistor=27, lf_capacitor=0),
      vco = dict( vco_post_scale = 0 ),
    ),
  }



  def set_frequency(self, clock, value, reconfig=False):
    """
    Sets the frequency of one of the output clocks.

    These are the equations that we use to derive the frequencies produced by
    the PLL.
    Fvco = Fin * (M/N)
    Fout = Fvco / C

    (1)  c0 = Fvco / C0 = Fin * (M/N) / C0
    (2)  c1 = Fvco / C1 = Fin * (M/N) / C1

    dividing (1)/(2):
    (3)  c0/c1 = C1/C0

    adding (1)+(2)
    (4) c0 + c1 = Fvco * ( 1/C0 + 1/C1 )
                = Fvco * ( (c0/c1)/C1 + 1/C1 )
                = (Fvco/C1) * (1 + (c0/c1))
    """
    F = self.frequencies
    if clock not in F:
      raise LookupError('Could not identify clock "{}"'.format(clock))

    C = int( round(F['vco'] / float(value)) )
    Fnew = F['vco'] / C

    if C <= 0:
      raise RuntimeError('cannot increase frequency more than vco={}'.format(F['vco']))
    elif C > 511:
      raise RuntimeError('cannot such a low frequency')
    elif value != Fnew:
      print 'WARNING:  setting to nearest acheivable frequency: {}'.format(Fnew)

    if Fnew == F[clock]:
      pass
    elif C == 1:
      self.set( clock, bypass=1, high_count=1, low_count=0, odd=0 )
    else:
      H = (C + 1)/2
      L = (C    )/2
      odd = 1
      if H == L:
        odd=0
      self.set( clock, bypass=0, high_count=H, low_count=L, odd=odd )

    if reconfig:
      self.reconfig()





class FakeFpga(object):
  def __init__(self):
    self.regcache = ReconfigRegister()
    self.pll_registers = dict(
      n = dict(
        high_count = 1,
        low_count = 1,
        bypass = 0,
        odd = 0,
        nominal = 1,
      ),
      m = dict(
        high_count = 8,
        low_count = 7,
        bypass = 0,
        odd = 1,
        nominal = 1,
      ),
      cp_lf = dict(
        lf_resistor = 27,
      ),
      vco = dict( vco_post_scale = 1 ),
      c0 = dict(
        high_count = 8,
        low_count = 7,
        bypass = 0,
        odd = 1,
      ),
      c1 = dict(
        high_count = 1,
        low_count = 0,
        bypass = 1,
        odd = 0,
      ),
    )

    self.pll_spc = 'reg'
    self.pll_addr = 0x0

  def write(self, spc, addr, data):
    assert self.pll_spc == spc, 'Wrong address space'
    assert self.pll_addr == addr, 'Wrong address'
    data = np.asarray( data, dtype=np.uint32 )
    if len( data ) != 1:
      raise RuntimeError('Should only write len()==1 arrays to pll register')

    r = ReconfigRegister( data[0] )
    if r.cmd == 'reconfig':
      print 'reconfigure!'
    elif r.cmd == 'reset':
      print 'reset pll reconfig'
    elif r.cmd == 'pll_reset':
      print 'reset pll'
    elif r.cmd == 'write':
      self.pll_registers[r.counter][r.param] = r.data
    elif r.cmd == 'read':
      self.regcache.value = r.value
      self.regcache.cmd = 0x001 # means not busy but locked
      self.regcache.data = self.pll_registers[r.counter][r.param]

  def read(self, spc, addr):
    assert self.pll_spc == spc, 'Wrong address space'
    assert self.pll_addr == addr, 'Wrong address'
    return self.regcache.value

def run_test():
  fpga = FakeFpga()

  r = Reconfig( fpga, fpga.pll_addr, Fin=10, output_counters=['c0', 'c1'] )
  print 'freqs: ', r.frequencies
  r.set_frequency( 'c0', 50 )
  print 'freqs: ', r.frequencies
  r.set_frequency( 'c1', 100 )
  print 'freqs: ', r.frequencies
  r.set_frequency( 'c1', 600 )
  print 'freqs: ', r.frequencies
  r.set_frequency( 'c0', 51 )
  print 'freqs: ', r.frequencies
  r.set_frequency( 'c0', 55 )
  print 'freqs: ', r.frequencies
  print 'status, busy: ', r.status, r.status.busy

if __name__ == '__main__':
  run_test()
