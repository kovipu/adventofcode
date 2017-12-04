#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as inputfile:
    spreadsheet = map(lambda row: row.split(), 
                      inputfile.read().splitlines())

spreadsheet = [[ int(n) for n in row ] for row in spreadsheet ]

print(sum(map(lambda row: max(row) - min(row), spreadsheet)))