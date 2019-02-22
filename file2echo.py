#! /usr/bin/python3

import os
import sys

file = sys.argv[1]
blocksize = sys.argv[2]

with open(file, 'rb') as f:
    data = f.read(64)
    for b in data:
        sys.stdout.write(hex(b).replace('0x', "\\x"))
    sys.stdout.write('\n')
    sys.stdout.flush()

