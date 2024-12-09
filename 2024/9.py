# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
results = []
lines = []
with open('input/input9.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append([int(ele) for ele in line.strip()])
        
print(lines)
#%%
def lastIndex(lst):
    return next(i for i in range(len(lst) - 1, -1, -1) if lst[i] != ".")


data = []
checksum = []
for n, line in enumerate(lines):
    data.append([])
    checksum.append(0)
    counter = 0
    for i,num in enumerate(line):
        # print(data[n])
        if (i%2 == 0):
            data[n].extend([counter] * num)
            counter += 1
        else:
            data[n].extend(["."] * num)
    print("data line", n, data[n])
    for j,dat in enumerate(data[n]):
        if(all(elem == "." for elem in data[n][j:])):
           break
        if (dat == "."):
            last = lastIndex(data[n])
            data[n][j], data[n][last] = data[n][last], data[n][j]
        checksum[n] += j*int(data[n][j])
    print("converted data line", n, data[n])
    print("checksum line", n, checksum[n])
    
# %% PART2

def chunk(lst, idx):
    if idx < 0 or idx >= len(lst):
        raise IndexError("Index out of range.")
    value = lst[idx]
    count = 1
    for i in range(idx + 1, len(lst)):
        if lst[i] == value:
            count += 1
        else:
            break

    return count

def lastChunk(lst, size, boundary):
    for i in range((len(lst)  - 1) , boundary-1, -1):
        if all(value == "." for value in lst[i:i+size]):
            return i


data = []
checksum = 0

counter = 0
for i,num in enumerate(lines[0]):
    if (i%2 == 0):
        data.extend([counter] * num)
        counter += 1
    else:
        data.extend(["."] * num)

data.reverse()
skip = 0
for j, value in enumerate(data):

    if j < skip:
        continue
    if value == ".":
        continue
    else:
        chunkSize = chunk(data, j)
        skip = j + chunkSize
        swapID = lastChunk(data, chunkSize, j + chunkSize)
        if swapID is not None:
            data[j:j + chunkSize], data[swapID: swapID + chunkSize] = data[swapID : swapID + chunkSize], data[j:j + chunkSize]
            
data.reverse()
for j, dat in enumerate(data):
    if dat != ".":
        checksum += j*dat
     
        
print("checksum", checksum)
