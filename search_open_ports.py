import argparse
import socket
from multiprocessing import Pool

parser = argparse.ArgumentParser('Search open ports via sockets')
parser.add_argument('begin', help='port to begin', type=int)
parser.add_argument('end', help='port to end', type=int)
parser.add_argument('host', help='target host')
parser.add_argument('--debug', help='debug mode', action='store_true')

args = parser.parse_args()


class PortScanner:

    def __init__(self, host: str, debug=False):

        self.host = host
        self.debug = debug

    def __call__(self, *args, **kwargs):
        self.scan_port(args[0])

    def scan_port(self, port: int):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:

            s.settimeout(1)
            s.connect((self.host, port))

        except Exception as e:
            if self.debug:
                print(e)

        finally:

            s.close()


if __name__ == '__main__':

    with Pool(40) as p:

        p.map(PortScanner(args.host, args.debug), range(args.begin, args.end + 1))
