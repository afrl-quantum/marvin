#!/usr/bin/env python
"""
Small example code of using marvin.ao module to talk to GX1649 card
"""
import marvin
b = marvin.ao.Board(0x030f)
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
