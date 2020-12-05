#!/usr/bin/python3

# Find two entries that sum to 2020 & multiply those two numbers

d = dict()

f = open('day1-input.txt', 'r')
for line in f.readlines():
    num = int(line.strip())
    if num not in d.keys():
        d[2020 - num] = None
    else:
        result = num * (2020 - num)
        break

print(f'part 1: {result}')

d = dict()
seen_nums = list()
result = None

# Find three entries that sum to 2020 & multiply those three numbers

f = open('day1-input.txt', 'r')
for line in f.readlines():
    num = int(line.strip())
    for seen_num in seen_nums:
        # add the two together and subtract from 2020
        # check if this number is in the expense report
        third_num = 2020 - (num + seen_num)

        # if so, multiply the three numbers together
        if third_num in d.keys():
            result = num * seen_num * third_num
            break

    seen_nums.append(num)
    d[num] = None

print(f'part 2: {result}')
