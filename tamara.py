#!/usr/bin/env python3
from __future__ import print_function
from Tamara.processor import TamaraProcessor

import sys


if __name__ == '__main__':
    if sys.version_info.major < 3:
        print('Tamara only supports Python3.')
        exit(2)
    else:
        TamaraProcessor()
