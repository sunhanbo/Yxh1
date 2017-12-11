# -*- coding: utf-8 -*-


import sys
import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'E:\A\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'E:\A\tcl\tk8.6'
base = 'Console'
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {

        # Sometimes a little fine-tuning is needed
        # exclude all backends except wx
        'includes': ['tensorflow', 'numpy', 'skimage', 'PyQt5', 'os']
        #'includes': []
    }
}

executables = [
    Executable('try.py', base=base)
]

setup(name='try_eg',
      version='1.0',
      description='Sample try script',
      executables=executables,
      options=options
      )

