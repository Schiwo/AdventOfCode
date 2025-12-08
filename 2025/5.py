# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
import numpy as np

with open('input/5.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().splitlines()
    blank_index = lines.index('')
    fresh_lines = lines[:blank_index]
    ingredient_lines = lines[blank_index+1:]
    fresh = fresh_lines
    ingredients = ingredient_lines
    
    
def convert_to_ranges(fresh_list):
    """Convert ['3-5', '10-14'] → [range(3,6), range(10,15)]"""
    ranges = []
    for item in fresh_list:
        start, end = map(int, item.split('-'))
        ranges.append(range(start, end + 1))
    return ranges

fresh = convert_to_ranges(fresh)
print("fresh", fresh)
print("ingredients", ingredients)

# %% PART 1
def count_fresh_ingredients(fresh, ingredients):
    count = 0
    for ing in ingredients:
        value = int(ing)
        if any(value in r for r in fresh):
            count += 1
    return count


print("Total fresh: ", count_fresh_ingredients(fresh, ingredients))

# %% PART 2

def count_unique_in_fresh(fresh):
    intervals = []
    for r in fresh:
        start = r.start
        end = r.stop - 1
        intervals.append((start, end))

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end + 1:  
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    total_unique = sum(end - start + 1 for start, end in merged)
    return total_unique

    
print("Total fresh: ", count_unique_in_fresh(fresh))

