import argparse


parser = argparse.ArgumentParser('Convert string to python function without quotes\nie : chr(99)+chr(111)+chr(117)+chr(99)+chr(111)+chr(117)')
parser.add_argument('str')

args = parser.parse_args()

s = args.str
i = 0

for c in s:
    i += 1
    code = ord(c)
    print('chr({code}){plus}'.format(code=code, plus='+' if i != len(s) else ''), end='')
print()
