#! /usr/bin/python3

import os
import sys

if len(sys.argv) < 2:
    print('Convert a binary file to printable hex chars (like \\x41\\x42)')
    print()
    print('Usage : file2echo <file> [<line_size>]'.format(sys.argv[0]))
    print('\tfile : file 2 convert')
    print('\tnumber of bytes by line (64 by default)')
    quit()

file = sys.argv[1]
if len(sys.argv) > 2:
    blocksize = int(sys.argv[2])
else:
    blocksize = 64

with open(file, 'rb') as f:
    while True:
        data = f.read(blocksize)
        if len(data) == 0:
            break
        for b in data:
            sys.stdout.write("\\x{:0>2x}".format(b))
        sys.stdout.write('\n')
        sys.stdout.flush()

