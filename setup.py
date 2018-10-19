#!/usr/bin/env python3

from setuptools import setup, find_packages
import os, sys

THIS_DIR = os.path.dirname( __file__ )
sys.path.insert(0, os.path.join(THIS_DIR, 'python'))

f = open('MANIFEST.in', 'w')
f.write('graft python/marvin\n')
f.close()

try :
  setup(
    name='marvin',
    version='0.1.0',
    author='Spencer E. Olson',
    author_email='olsonse@umich.edu',
    description='Python wrappers for Marvin Test Gx* libraries',
    long_description=
      'Marvin Test provides analog, digital, and FPGA hardware.  This package '
      'provides simple Python bindings using Python-Ctypes.',
    url='https://github.com/afrl-quantum/marvin',
    license='MIT',
    packages=find_packages('python'),
    package_dir = {'' : 'python'},
    include_package_data=True,
  )
finally:
  os.unlink('MANIFEST.in')
