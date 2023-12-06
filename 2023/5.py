# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

# with open("input\\input5.txt") as f:
with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

seeds = changeListDatatype(re.findall(r'\d+', lines[0]))
maps = []
mapID = -1

locations = []

def mapper(seed):
    step = 0
    pos = seed    
    while (step < len(maps)):
        for y in range(0, len(maps[step])):
            if (pos in range(maps[step][y][1], maps[step][y][1] + maps[step][y][2])):
                pos = pos + (maps[step][y][0] - maps[step][y][1])
                break
        step += 1

    return(pos)

for x in range(1, len(lines)):
    if(re.search(r'(map)', lines[x])):
        maps.append([])
        mapID += 1
    elif(lines[x]):
        maps[mapID].append(changeListDatatype(re.findall(r'\d+', lines[x])))
        maps[mapID]
        
    
# for y in range(0, len(maps)):
#     maps[y] = sorted(maps[y], key=lambda z: z[1])

# for seed in range(0, len(seeds)):
#     locations.append(mapper(seeds[seed]))
    
# print("Results Part 1: " + str(min(locations)))



# Part 2
seeds2 = []
locations2 = []
print(seeds)

for i in range(0,len(seeds),2):
    seeds2.append((seeds[i], seeds[i]+seeds[i+1]))
    print(seeds2)
  
def mapper2(seed):
    pos = []
    for direction, start, length in maps:
        if start <= seed < start + length:

            pos.append(seed + direction - start)
            break
        else:
            pos.append(seed)
            

def mapper3(seeds):
    
    step = 0
    while (step < len(maps)):
        for y in range(0, len(maps[step])):
            if (pos in range(maps[step][y][1], maps[step][y][1] + maps[step][y][2])):
                pos = pos + (maps[step][y][0] - maps[step][y][1])
                break
        step += 1

    return(pos)
    
    
pos = []
while len(seeds2) > 0:
    lowerB, upperB = seeds2.pop()
    for direction, start, length in maps:
        overlapStart = max(lowerB, start)
        overlapEnd = min(upperB, start + length)
        if overlapStart < overlapEnd:
            pos.append((overlapStart - start + direction, overlapEnd - start + direction))
            if overlapStart < start:
                seeds2.append((lowerB, overlapStart))
            if overlapEnd < start + length:
                seeds2.append((overlapEnd, upperB))
            break
    else:
        pos.append((lowerB, upperB))
        
            
            
# subArrays = seeds2
# subMins = [None] * len(subArrays)

# for s in range(0, 10):
#     subrange = subArrays[s]
#     print(subrange)
#     loc = []
#     for seed in subrange:
#         loc.append(mapper(seed))
#     subMins[s] = min(loc)

# print(subMins)
# minRange = subArrays[subMins.index(min(subMins))]
# rangeLen = len(minRange)    

# print("initial check finished:")
# print(minRange)

# while (rangeLen > 100000):
#     subArrays = np.array_split(np.array(minRange),10)
#     subMins = [None] * len(subArrays)
    
#     for s in range(0, 10):
#         sub = subArrays[s]
#         subrange = range(min(sub), max(sub) + 1, 5000)
#         print(subrange)
#         loc = []
#         for seed in subrange:
#             loc.append(mapper(seed))
#         subMins[s] = min(loc)
    
#     minRange = subArrays[subMins.index(min(subMins))]
#     rangeLen = len(minRange)
#     print("cycle finished")
            
# for seed in range(0, len(minRange)):
#     locations2.append(mapper(minRange[seed]))
            
# print(min(locations2))