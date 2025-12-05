# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%% PART 1

with open('input/1.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
turns = lines
positions = [50]
neutrals = 0
print(turns)

# %% PART 1


def parse_direction(s):
    direction = s[0]
    value = int(s[1:])
    if direction == 'L':
        return -value
    elif direction == 'R':
        return value
    else:
        raise ValueError("Input must start with 'L' or 'R'.")


def dial(arr, n):
    last = arr[-1]
    result = last + n
    while result < 0:
        result += 100
    while result > 99:
        result -= 100
    arr.append(result)
    return arr


for i in range(len(turns)):
    turns[i] = parse_direction(turns[i])
    positions = dial(positions, turns[i])

    
print("0 positions:", positions.count(0))


# %% PART 2

positions = [50]

def dial2(arr, n):
    last = arr[-1]
    result = last + n
    ntrl = 0
    
    if (n == 0):
        return arr, ntrl
    

    while result < 0:
        result += 100
        ntrl += 1
    while result > 99:
        result -= 100
        ntrl += 1
        
    if n < 0: 
        if result == 0:
            ntrl += 1
        elif last == 0:
            ntrl -= 1


    arr.append(result)
    return arr, ntrl

for i in range(len(turns)):
    ntrl = 0
    positions, ntrl = dial2(positions, turns[i])
    neutrals += ntrl
    print(turns[i], neutrals)

print("neutral positions:", neutrals)
