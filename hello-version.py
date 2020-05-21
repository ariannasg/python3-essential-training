#! usr/bin/env python3

import platform
import sys
import os

print('This is my python version: {}'.format(platform.python_version()))
print('This is my sys platformL {}'.format(sys.platform))
print('This is my os name: {}'.format(os.name))
print('This is my working directory {}'.format(os.getcwd()))

# CONSOLE OUTPUT:
# This is python version 3.8.3
# This is sys platform darwin
# This is os name posix

