#!/usr/bin/env python3

# just a basic and simple script.
# Use hashcat if you want be serious !

from passlib.hash import bcrypt
import os
import sys

if len(sys.argv) < 3:
    print('Usage : python3 crack.py <dictionnary> <hashes file>')
    quit()

dico_file = sys.argv[1]
hashes_file = sys.argv[2]


def update_display(new_value, total):
    val = int(new_value / total * 100)
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('=' * (int(val / 5) - 1) + '>', val))
    sys.stdout.flush()


# encoding iso for work with rockyou, stange.
with open(dico_file, "r", encoding="ISO-8859-1") as f:
    length = sum(1 for line in f)

with open(hashes_file, 'r') as f:
    hashes = f.read().splitlines()

index = 0

with open(dico_file, "r") as f:
    sys.stdout.write("[%-20s] 0%%" % '')
    sys.stdout.flush()

    for word in f:
        if not word:
            break

        word = word.rstrip('\n')

        update_display(index, length)

        index += 1

        for h in hashes:
            correct = bcrypt.verify(word, h)
            if correct:
                print('\nFind hash ! : {} => {}'.format(h, word))

    update_display(length, length)
    sys.stdout.write('\n')
    sys.stdout.flush()
