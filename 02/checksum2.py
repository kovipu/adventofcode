#!/usr/bin/env python3

from itertools import combinations
# from functools import filter
import sys

with open(sys.argv[1]) as inputfile:
    spreadsheet = map(lambda row: row.split(), 
                      inputfile.read().splitlines())

def calculate_checksum(row):
    row = map(int, row)
    return [a/b if a>b else b/a for a,b in combinations(row, 2) if a%b==0 or b%a==0][0]

print(sum(map(calculate_checksum, spreadsheet)))
