#!/usr/bin/python3

# Find two entries that sum to 2020 & multiply those two numbers together

d = dict()

f = open('day1-input.txt', 'r')
for line in f.readlines():
    number = int(line.strip())
    if number not in d.keys():
        d[2020 - number] = None
    else:
        result = number * (2020 - number)
        break

print(result)
