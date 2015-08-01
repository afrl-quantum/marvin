#!/bin/bash
# vim: et:sw=2:ts=2:nowrap
includedir=/usr/include/MarvinTestSolutions
mkdir -p python/marvin/clib clib.tmp
for i in $includedir/*; do
  name=$(basename ${i//.h})
  h2xml.py -c $i -o clib.tmp/$name.xml
  xml2py.py clib.tmp/$name.xml -l$name -o python/marvin/clib/$name.py
done
