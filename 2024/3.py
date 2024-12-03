# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import re

#%% PART 1

with open('input/input3.txt', 'r') as file:
    content = file.read()

#%% 
regex_mul = r"mul\(\d+,\d+\)"
 
results=[]      
matches = re.findall(regex_mul, content)
for match in matches:
    print(match)
    x, y = map(int, re.findall(r"\d+", match))
    results.append(x * y)
total_sum = sum(results)



print(f"Sum of values: {total_sum}")


#%% Part 2
file_path = 'input/input3.txt'
with open(file_path, 'r') as file:
    content = file.read()
    
#%%
content = content.replace("\n", "")
content = re.sub(r"don't\(\).*?(do\(\)|$)", "", content)

regex_mul = r"mul\(\d+,\d+\)"
 
results=[]      
matches = re.findall(regex_mul, content)
for match in matches:
    print(match)
    x, y = map(int, re.findall(r"\d+", match))
    results.append(x * y)
total_sum = sum(results)



print(f"Sum of values: {total_sum}")