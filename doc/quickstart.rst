.. _quickstart:

Quick Start
============
Marvin Test Solutions, Inc. develops various digital, analog, and FPGA boards
that can easily be integrated into an experimental apparatus.

********************
Simple Analog Output
********************
This is a simple example for generating simply output voltages using a GX1649
card.

.. code-block:: python

  #!/usr/bin/env python
  """
  Small example code of using marvin.ao module to talk to GX1649 card
  """
  import marvin
  b = marvin.ao.Board(0x020a)
  groupA = b[0] # or you can do groupA = b['a']
  cA0 = groupA[0]

  table = list()
  for V in xrange(-5,6):
    # following line implicitly calls GxAoSetChannelVoltage
    cA0.voltage = V
    # cA0.voltage can also be used as property--calls GxAoGetChannelVoltage
    table.append( [V, cA0.voltage, input('enter oscilloscope value:  ')] )

  print 'values entered vs voltage register vs values measured:'
  print table


*********************
Waveform Output Example
*********************
This is a simple example for specifying a waveform that will be executed.

.. code-block:: python

  #!/usr/bin/env python

  from marvin import ao
  import numpy as np

  def static_fun(xi,xf,step=0.00048, t=1):
    for i in xrange(xi,xf):
      c0.voltage = i*step
      print '{}\t{}'.format(i*step, c0.voltage)
      time.sleep(t)

  #for i in xrange(10):
  #    static_fun(0,4,t=1,step=0.000458)


  def mk_sawtooth(group, N=300, duty=0.5, channels=xrange(0,16)):
    group.waveform_channels = channels
    group.per_channel_length = N
    for i in group.waveform_channels:
      n0 = int(duty * N)
      n1 = int((1-duty) * N)
      group[i].waveform = np.r_[0:10:(1j*n0), 10:0:(1j*n1)]/float(1+i)
      #print 'i,waveform: ', i, group[i].waveform

  def main():
    b = ao.Board(0x020a)
    b.reset()
    gA = b['a']
    if raw_input('Test Trigger instead of clock (y/n): ') == 'y':
      gA.clock = ('internal', 1e4)
      gA.trigger_source = 'TRIG/7'
    else:
      gA.trigger_source = 'software_only'
      gA.clock = ('TRIG/1')
    mk_sawtooth(gA)
    gA.arm()
    if gA.trigger_source == 'software_only':
      raw_input('press-enter to software trigger')
      gA.trigger()
    raw_input('press-enter to stop/quit')
    gA.disarm()


  if __name__ == '__main__':
    main()
