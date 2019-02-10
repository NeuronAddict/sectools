#!/usr/bin/python3

for c in range(0, 256):
	print('\\x{}'.format(hex(c)[2:].zfill(2)), end='')
