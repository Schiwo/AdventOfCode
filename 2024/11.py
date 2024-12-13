# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""


#%% PART 1
results = []
line = []
with open('input/input11.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        line = list(map(int, line.strip().split()))
        
print(line)

# %%

def sort(lst):
    zeros = []
    evenDigits = []
    rest = []
    for number in lst:
        if number == 0:
            zeros.append(number)
        elif len(str(number)) % 2 == 0:
            evenDigits.append(number)
        else:
            rest.append(number)
    return [zeros, evenDigits, rest]

def split(numbers):
    result = []
    for n in numbers:
        s = str(n)
        mid = len(s) // 2
        result.extend((int(s[:mid]), int(s[mid:])))
    return result

def flatten(xss):
    return [x for xs in xss for x in xs]


def blink(lst):
    zeros = lst[0]
    evenDigits = lst[1]
    rest = lst[2]
    
    newLst =[]
    
    newLst.extend([x + 1 for x in zeros])
    newLst.extend(split(evenDigits))
    newLst.extend([x * 2024 for x in rest])
    
    return(sort(newLst))
# %%

blinkLine = sort(line)
for i in range(0, 25):
    blinkLine = blink(blinkLine)
    print("blink", i+1)
    blinkLine[0] = []


print(len(flatten(blinkLine)))

# %% PART 2 resolved with the help =( https://topaz.github.io/paste/#XQAAAQBmAQAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponKxDhfDpmpp1XaSM15emS/r8eKIsi8OyRU1yttx/bMBsS4XZHZN6NkMdw4WSJvzKz7a+8Nmsp1b8xwfTg6quN6qTJ245hV4tLxhD1trmPHMhqawzEcRNiQ8xJHXCVugAUaFTdzmvC2oYMDQlYGJBYjguH/wbIC+3zdU7i9gW3/6LzoHPeOKZcciKOFy9898nylpv0qpiHf5aI65VOrFLGBlbk8xkjU4EfRE2oapEMPdFbSjkN6tJ6L4+GQ6HEWv/lwxQA
from functools import cache
from math import floor, log10

@cache
def count(x, d=75):
    if d == 0: return 1
    if x == 0: return count(1, d-1)

    l = floor(log10(x))+1
    if l % 2: return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1)+
            count(x %  10**(l//2), d-1))

print(sum(map(count, line)))