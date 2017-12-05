#!/usr/bin/env python3

import sys

try:
    f = sys.argv[1]
except:
    f = "passphrases.txt"

with open(f) as inputfile:
    passphrases = inputfile.read().splitlines()

def validate_passphrase(passphrase):
    words = passphrase.split()
    return all([ words.count(w) == 1 for w in words ])

print(len(list(filter(validate_passphrase, passphrases))))