# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%% PART 1

# with open('input/2.txt', 'r') as file:
with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
parts = [p for p in lines[0].replace("\n", "").split(",") if p]
ids = [list(map(int, part.split("-"))) for part in parts]


print(ids)
# %% PART 1
numsum = 0

def find_repeated_numbers(a: int, b: int):
    repeated = []
    for n in range(a, b + 1):
        s = str(n)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                repeated.append(n)
    return repeated



for idRange in ids:
    # print(idRange)
    repeated = find_repeated_numbers(idRange[0], idRange[1])
    print(repeated)
    for num in repeated:
        numsum += num
        
print("sum of repeated numbers:", numsum)

# %% PART 2

numsum2 = 0

def is_any_repeated(n: int) -> bool:
    s = str(n)
    length = len(s)

    # Try all possible part lengths
    # At least 2 parts → part_len max is length // 2
    for part_len in range(1, length // 2 + 1):
        if length % part_len != 0:
            continue  # can't split evenly into this part length

        part = s[:part_len]
        if part * (length // part_len) == s:
            return True

    return False

def find_repeated_numbers2(a: int, b: int):
    repeated = []
    for n in range(a, b + 1):
        if is_any_repeated(n):
            repeated.append(n)
    return repeated



for idRange in ids:
    # print(idRange)
    repeated = find_repeated_numbers2(idRange[0], idRange[1])
    print(repeated)
    for num in repeated:
        numsum2 += num
        
print("sum of repeated numbers:", numsum2)