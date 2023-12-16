# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:03:46 2023

@author: morit
"""


import regex as re
import numpy as np

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input11.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]

universe = []

for line in lines:
    universe.append([x for x in line])
    

universe = np.array(universe)
emptyX = []
emptyY = []
galaxies = []

# for x in range(len(universe[0,:])):
#     if len(set(universe[:, x])) == 1:
#         emptyX.append(x)

# for i in range(len(emptyX)):
#     universe = np.insert(universe, emptyX[i]+i, universe[:, emptyX[i]+i], axis=1)



# for y in range(len(universe[:,0])):
#     if len(set(universe[y, :])) == 1:
#         emptyY.append(y)

# for i in range(len(emptyY)):
#     universe = np.insert(universe, emptyY[i]+i, universe[emptyY[i]+i, :], axis=0)


# for y in range(len(universe[:,0])):
#     for x in range(len(universe[0,:])):
#         if universe[y,x] == "#":
#             galaxies.append((y,x))
#             universe[y,x] = len(galaxies)
   
# print(universe) 
 
   
 
# def distance(gal1, gal2):
#     # print("gal1 coord")
#     # print(gal1)
#     # print("gal2 coord")
#     # print(gal2)
#     yDist = abs(gal2[0]-gal1[0]) 
#     xDist = abs(gal2[1]-gal1[1])
#     # print("x: " + str(xDist))
#     # print("y: " + str(yDist))
#     return (yDist +  xDist)
    
# dist = []
# for i in range(len(galaxies)-1):
#     dist.append([])
#     for j in range(i+1, len(galaxies)):
#         dist[i].append(distance(galaxies[i], galaxies[j]))
#     dist[i] = sum(dist[i])
    
    
# print("Part1: " + str(sum(dist)))
#Part 2


growth = 1000000 - 1 


for x in range(len(universe[0,:])):
    if len(set(universe[:, x])) == 1:
        emptyX.append(x)
        

for y in range(len(universe[:,0])):
    if len(set(universe[y, :])) == 1:
        emptyY.append(y)

for y in range(len(universe[:,0])):
    for x in range(len(universe[0,:])):
        if universe[y,x] == "#":
            galaxies.append((y,x))
            universe[y,x] = len(galaxies)
            

print(galaxies)

def distance2(gal1, gal2):
    # print("gal1 coord")
    # print(gal1)
    # print("gal2 coord")
    # print(gal2)
    yRange = range(*sorted([gal2[0], gal1[0]]))
    xRange = range(*sorted([gal2[1], gal1[1]]))
    yJumps = len(set(yRange) & set(emptyY))*growth
    xJumps = len(set(xRange) & set(emptyX))*growth
    print("y " + str(yJumps))
    print(set(yRange))
    print(set(emptyY))
    print("x " + str(xJumps))
    print(set(xRange))
    print(set(emptyX))
    yDist = len(yRange) + yJumps
    xDist =  len(xRange) + xJumps
    # print("x: " + str(xDist))
    # print("y: " + str(yDist))
    return (yDist +  xDist)

dist = []
for i in range(len(galaxies)-1):
    dist.append([])
    for j in range(i+1, len(galaxies)):
        print(" ")
        print("Gal1 " + str(i+1))
        print("Gal1 " + str(j+1))
        dist[i].append(distance2(galaxies[i], galaxies[j]))
    dist[i] = sum(dist[i])
    
print(universe)
print(sum(dist))