import argparse
import codecs


def convert(data: str, double_dash=False):
    out = ''
    for b in data:
        out += "{dash}\\x{payload}".format(dash='\\' if double_dash else '', payload=codecs.encode(b.encode(), "hex").decode())
    return out


if __name__ == "__main__":

    parser = argparse.ArgumentParser('Convert string to bash encoded string (\x45\x20)')
    parser.add_argument('str', help='String to encode')
    parser.add_argument('--double', help='print double slash', action='store_true')

    args = parser.parse_args()

    print(convert(args.str, args.double))
