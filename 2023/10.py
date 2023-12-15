# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:03:46 2023

@author: morit
"""


import regex as re
import numpy as np

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input10.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]

laby = []

for line in lines:
    laby.append([x for x in line])


laby = np.array(laby)


def navigate(past, current):
    if past == current:
        raise "past == current"
    oY = past[0]
    oX = past[1]
    nY = current[0]
    nX = current[1]
    if laby[current] == "-":
         future = (nY, (nX + (nX - oX)))
    elif laby[current] == "|":
        future = ((nY + (nY - oY)), nX)
    elif laby[current] == "L":
        if oX == nX:
            future = (oY + 1, oX + 1)
        else:
            future = (oY - 1, oX - 1)
    elif laby[current] == "J":
        if oX == nX:
            future = (oY + 1, oX - 1)
        else:
            future = (oY - 1, oX + 1)
    elif laby[current] == "7":
        if oX == nX:
            future = (oY - 1, oX - 1)
        else:
            future = (oY + 1, oX + 1)
    elif laby[current] == "F":
        if oX == nX:
            future = (oY - 1, oX + 1)
        else:
            future = (oY + 1, oX - 1)
    elif laby[current] == "S":
        future = current
    else:
        future = (-1,-1)
    return (current, future)

def findConnection(start):
    sY = start[0]
    sX = start[1]
    posO = []
    posO.append((sY-2, sX))
    posO.append((sY+2, sX))
    posO.append((sY, sX-2))
    posO.append((sY, sX+2))
    posO.append((sY-1, sX-1))
    posO.append((sY-1, sX+1))
    posO.append((sY+1, sX-1))
    posO.append((sY+1, sX+1))
    
    posN = []
    posN.append((sY-1, sX))
    posN.append((sY+1, sX))
    posN.append((sY, sX-1))
    posN.append((sY, sX+1))

    
    for pO in posO:
        for pN in posN:
            if navigate(pO, pN)[1] == tuple(start):
                return pN
    


def maxDistance():
    start1 = changeListDatatype(np.where(laby == "S"))
    start2 = findConnection(start1)
    pos = [start1, 
           start2]
    steps = 1
    
    while (pos[1] != tuple(start1)):
        pos = navigate(pos[0], pos[1])
        steps += 1
        
        
    return(steps/2)
    
    
# print(maxDistance())
# print(navigate((1,2), (1,1)))

#Part 2
copy2 = np.copy(laby)

def markLaby():
    markedLaby = np.copy(laby)
    start1 = np.where(laby == "S")
    start2 = findConnection(start1)
    markedLaby[start2] = 1
    pos = [start1, 
           start2]
    steps = 1
    
    while (pos[1] != tuple(start1)):
        pos = navigate(pos[0], pos[1])
        markedLaby[pos[1]] = 1
    
    return markedLaby

def countArea(mLaby):
    counter = 0
    copy = np.copy(mLaby)
    for x in range(len(mLaby[0,:])):
        openRight = False
        openLeft = False
        counting = False
        element = -1
        maxElement = np.count_nonzero(mLaby[:,x] == "1")
        for y in range(len(mLaby[:,0])):
            if mLaby[y,x] == "1":
                element += 1
                if laby[y,x] == "-":
                    counting = not counting
                elif laby[y,x] == "F":
                    openRight = True
                elif laby[y,x] == "7":
                    openLeft = True
                elif laby[y,x] == "L":
                    if (openLeft == True):
                        counting = not counting
                        openLeft = False
                        openRight = False
                    else:
                        openRight = False
                        openLeft = False
                elif laby[y,x] == "J":
                    if (openRight == True):
                        counting = not counting
                        openRight = False
                        openLeft = False
                    else:
                        openLeft = False
                        openRight = False
                if counting:
                    copy[y,x] = "C"
                else:
                    copy[y,x] = "N"
                # if x == 2:
                    # print(laby[y,x])
                    # print("oright:" + str(openRight))
                    # print("oleft:" + str(openLeft))
                           
            elif(counting and (maxElement - element) >= 2):
                copy[y,x] = "X"
                copy2[y,x] = "X"
                counter += 1
            else:
                copy[y,x] = " "
                copy2[y,x] = " "
    return counter
    
print(countArea(markLaby()))
