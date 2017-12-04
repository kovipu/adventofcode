#!/usr/bin/env python3

import sys

x = sys.argv[1]

value = 0

for (a, b) in zip(x[:-1], x[1:]):
    if a == b:
        value += int(a)

if x[0] == x[-1]:
    value += int(x[0])

print(value)
