#!/bin/bash
# vim: et:sw=2:ts=2:nowrap
H2XML=h2xml
XML2PY=xml2py
includedir=/usr/include/MarvinTestSolutions

DEFINES="-D_LP64" # this is only valid for a 64-bit machine

mkdir -p python/marvin/clib clib.tmp
for i in $includedir/*; do
  name=$(basename ${i//.h})
  ${H2XML} ${DEFINES} -c $i -o clib.tmp/$name.xml
  ${XML2PY} clib.tmp/$name.xml -l$name -o python/marvin/clib/$name.py
done

rm -rf clib.tmp
