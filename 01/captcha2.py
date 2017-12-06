#!/usr/bin/env python3

import sys

x = sys.argv[1]

value = 0
OFFSET = len(x) // 2

for i, v in enumerate(x):
    if v == x[(i + OFFSET) % len(x)]:
        value += int(v)

print(value)