#! /usr/bin/env python3

import argparse
import sys
import binascii

parser =argparse.ArgumentParser('Convert file to hexadecilam litteral (ie: for mysql)')
parser.add_argument('file', help='file to convert')
parser.add_argument('--add_0x', help='Add 0x at start of result', action='store_true')

args = parser.parse_args()



with open(args.file, 'rb') as f:    

    content = f.read()

    print('{}{}'.format('0x' if args.add_0x else '', binascii.hexlify(content).decode()))
