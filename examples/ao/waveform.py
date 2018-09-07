#!/usr/bin/env python

from marvin import ao
import numpy as np

from six.moves import input

def static_fun(xi,xf,step=0.00048, t=1):
  for i in range(xi,xf):
    c0.voltage = i*step
    print('{}\t{}'.format(i*step, c0.voltage))
    time.sleep(t)

#for i in xrange(10):
#    static_fun(0,4,t=1,step=0.000458)


def mk_sawtooth(group, N=300, duty=0.5, channels=range(0,16)):
  group.waveform_channels = channels
  group.per_channel_length = N
  for i in group.waveform_channels:
    n0 = int(duty * N)
    n1 = int((1-duty) * N)
    group[i].waveform = np.r_[0:10:(1j*n0), 10:0:(1j*n1)]/float(1+i)
    #print('i,waveform: ', i, group[i].waveform)

def main():
  b = ao.Board(0x020a)
  b.reset()
  gA = b['a']
  if input('Test Trigger instead of clock (y/n): ') == 'y':
    gA.clock = ('internal', 1e4)
    gA.trigger_source = 'TRIG/7'
  else:
    gA.trigger_source = 'software_only'
    gA.clock = ('TRIG/1')
  mk_sawtooth(gA)
  gA.arm()
  if gA.trigger_source == 'software_only':
    input('press-enter to software trigger')
    gA.trigger()
  input('press-enter to stop/quit')
  gA.disarm()


if __name__ == '__main__':
  main()
