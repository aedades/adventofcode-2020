#!/usr/bin/python3

import re

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Lowest & highest number of times the given character can appear

# How many passwords are valid according to their policies?

valid = 0

f = open('day2-input.txt', 'r')
for line in f.readlines():
    regex = '(\d+)-(\d+) (\S): (\S+)'

    m = re.match(regex, line)
    min = int(m[1])
    max = int(m[2])
    char = m[3]
    password = m[4]
    count = 0

    for c in password:
        if c == char:
            count += 1
    if count >= min and count <= max:
        valid += 1

print(f'part 1: {valid}')

valid = 0

# Numbers indicate two positions, exactly one position must be the given character

f = open('day2-input.txt', 'r')
for line in f.readlines():
    regex = '(\d+)-(\d+) (\S): (\S+)'

    m = re.match(regex, line)
    pos_1 = int(m[1])
    pos_2 = int(m[2])
    char = m[3]
    password = m[4]

    if (password[pos_1 - 1] == char) != (password[pos_2 - 1] == char):
        valid += 1

print(f'part 2: {valid}')
