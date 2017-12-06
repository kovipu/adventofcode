#!/usr/bin/env python3

import sys

pointer = 0
count = 0

with open(sys.argv[1]) as inputfile:
    instructions = list(map(int, inputfile.read().splitlines()))

while 0 <= pointer < len(instructions):
    i = instructions[pointer]
    instructions[pointer] += 1
    pointer += i
    count += 1

print(count)
