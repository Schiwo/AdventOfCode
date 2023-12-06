# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input5.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

seeds = changeListDatatype(re.findall(r'\d+', lines[0]))
maps = []
mapID = -1

locations = []

def mapper(seedInput, step):
    pos = []
    while len(seedInput) > 0:
        seed = seedInput.pop()
        for direction, start, length in maps[step]:
            if start <= seed < start + length:
                pos.append(seed + (direction - start))
                break
        else:
            pos.append(seed)
    
    step += 1
    if step < len(maps):
        return(mapper(pos, step))
    else:
        return(pos)

for x in range(1, len(lines)):
    if(re.search(r'(map)', lines[x])):
        maps.append([])
        mapID += 1
    elif(lines[x]):
        maps[mapID].append(changeListDatatype(re.findall(r'\d+', lines[x])))
        maps[mapID]
            
            
for y in range(0, len(maps)):
    maps[y] = sorted(maps[y], key=lambda z: z[1])


    
print("Results Part 1: " + str(min(mapper(seeds, 0))))



# Part 2
seeds2 = []
locations2 = []

for i in range(0,len(seeds),2):
    seeds2.append((seeds[i], seeds[i]+seeds[i+1])) 
  
def mapper2(seedInput, step):
    print(step)
    pos = []
    counter = 0
    while len(seedInput) > 0:
        counter += 1
        if counter == 1000:
            raise("error")
        seedLowerB, seedUpperB = seedInput.pop()
        for direction, start, length in maps[step]:
            olapLowerB = max(seedLowerB, start)
            olapUpperB = min(seedUpperB, start + length) 
            if olapLowerB < olapUpperB:
                pos.append((olapLowerB + (direction - start), olapUpperB + (direction - start)))
                if olapLowerB < start :
                    seedInput.append((seedLowerB, olapLowerB))
                if olapUpperB > start + length:
                    seedInput.append((olapUpperB, seedUpperB))

                break
        else:
            pos.append((seedLowerB, seedUpperB))
    
    step += 1
    if step < len(maps):
        return(mapper2(pos, step))
    else:
        return(pos)

x = mapper2(seeds2, 0)
print("Results Part 2: " + str(min(min(x))))
            
