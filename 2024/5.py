# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import matplotlib.pyplot as plt


#%% PART 1
lines = []
with open('input/input5.txt', 'r') as file:
    for line in file:
        lines.append(line)

splitAt = lines.index("\n")

rulesInput = lines[:splitAt]
updateInput = lines[splitAt + 1:]

#%%
rules = {}

for rule in rulesInput:
    key, value = map(int, rule.split('|'))  # Parse the line into key and value
    if key not in rules:
        rules[key] = set()  # Initialize a set for the key
    rules[key].add(value)  # Add the value to the 

#%%
updates =  []
for update in updateInput:
    updates.append(list(map(int, update.split(','))))

#%%
def center(lst):
    if len(lst) % 2 == 0:
        raise ValueError("The list does not have an odd number of elements.")
    center_index = len(lst) // 2
    return lst[center_index]

#%%

def check(update):
    for i, n in enumerate(update):
        if any(element in rules.get(n ,{}) for element in update[:i]):
            return False
    return True

#%%
sum = 0
for update in updates:
    if(check(update)):
        sum += center(update)
        
print(sum)

#%% PART 2

def check2(update):
    updated = False
    while True:
        for i, n in enumerate(update):
            if any(element in rules.get(n ,{}) for element in update[:i]):
                updated = True
                movingElement = update.pop(i)
                # print(f"Update: {update}")
                # print(f"False element: {n}")
                for original_index, reversed_index in zip(
                    reversed(range(len(update[:i]))),
                    range(len(update[:i]))
                ):
                    if all(elem not in rules[n] for elem in update[:i][:reversed_index]):
                        new_position = original_index
                        break
                update.insert(new_position, movingElement)
                break
            
        else:
            break
    
    if(updated):           
        return update
    else:
        return False
 
#%%       
updates =  []
for update in updateInput:
    updates.append(list(map(int, update.split(','))))

sum = 0
for update in updates:
    if(check2(update)):
        sum += center(update)
        
print(sum)