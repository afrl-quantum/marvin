#!/usr/bin/env python
"""
Small example code of using marvin.ao module to talk to GX1649 card
"""
from six.moves import input

import marvin
b = marvin.ao.Board(0x020a)
groupA = b[0] # or you can do groupA = b['a']
cA0 = groupA[0]

table = list()
for V in range(-5,6):
  # following line implicitly calls GxAoSetChannelVoltage
  cA0.voltage = V
  # cA0.voltage can also be used as property--calls GxAoGetChannelVoltage
  table.append( [V, cA0.voltage, eval(input('enter oscilloscope value:  '))] )

print('values entered vs voltage register vs values measured:')
print(table)
