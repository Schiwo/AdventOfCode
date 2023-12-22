# # # -*- coding: utf-8 -*-
# # """
# # Created on Thu Dec  7 12:03:46 2023

# # @author: morit
# # """


import regex as re
import numpy as np

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

def getIt(lst, start=0):
    return range(start, len(lst))

with open("input\\input12.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]

springs = []
records = []
solutions = []

# for line in lines:
#     springs.append(re.findall(r'[.?#]', line))
#     records.append(changeListDatatype(re.findall(r'\d+', line)))


# for i in range(len(springs)):
    # counter = 0
    # for j in range(len(springs[i])):
    #     if springs[i][j] == ".":
    #         counter = 0
    #         springs[i][j] = counter
    #     elif springs[i][j] == "?":
    #         counter = 0
    #     elif springs[i][j] == "#":
    #         counter += 1 
    #         springs[i][j] = counter
    #         for c in range(counter):
    #             springs[i][j-c] = counter
 
    
# def createCombos(sprngs, rules, j=0):

#     for i in getIt(sprngs, j):
#           sps = sprngs.copy()
#           sprng = sps[i]
#           # print(changeListDatatype(sps, str))
#           sprID = []
#           for s in getIt(sps):
#               if s == i:
#                   sprID.append("_")
#               else:
#                   sprID.append(" ")
#           # print(sprID)
         
#           if sprng == 0:
#               if check(sps[:i+1], rules):
#                   continue
#               else:
#                   return 0
             
#           elif sprng == "?":
#               # print("no new spring")
#               sps[i] = 0
#               noSpringLine = createCombos(sps, rules, i)
#               sprngSum = 0
#               prev = int()
#               for x in sprngs:
#                   if not isinstance(x,str):
#                       if x == prev:
#                           continue
#                       else:
#                           prev = x
#                           sprngSum += x
#                   else:
#                       prev = 0
             
#               if sprngSum < sum(rules):
#                   # print("add spring")
#                   if i > 0:
#                       sps[i] = 1 + sps[i-1]
                     
#                   else:
#                       sps[i] = 1
#                   sps[i - sps[i] + 1: i + 1] = [sps[i]] * sps[i]
    
#                   if i < len(sps) - 1:
#                       if type(sps[i+1]) == int:
#                           sps[i - sps[i] + 1: i + 1] = [sps[i] + sps[i+1]]*sps[i]
#                           sps[i+1: i + sps[i+1] + 1] = [sps[i] ]*sps[i+1]
#                   springLine = createCombos(sps, rules, i)
#               else: 
#                   # print("too many springs")
#                   springLine = 0
#               return (noSpringLine + springLine)
             
    
#     if check(sprngs, rules, True):
#         # print(sprngs)
#         return 1
#     else:
#         return 0


# def check(toBeChecked, rules, final=False):
#     r = 0
#     i = 0
#     while i < len(toBeChecked):
#         sprng = toBeChecked[i]
#         if type(sprng) == int:
#             if sprng > 0:
#                 if r >= len(rules):
#                     # print("FALSE")
#                     return False
#                 # print(str(sprng) + " should be " + str(rules[r]))
#                 if sprng == rules[r]:
#                     r += 1
#                     i += sprng
#                     continue
#                 else:
#                     # print("FALSE")
#                     return False
            
#         i += 1
#         continue
     
#     # print(toBeChecked)
#     if final:
#         if r == len(rules):
#             # print("CORRECT SOLUTION")
#             return True
#         else:
#             # print("FALSE UNUSED RULES")


#             return False
#     else:
#         # print("allowed")
#         return True
   
     
# for i in range(len(springs)):
# # for i in range(921,922):
#     print(" ")
#     print("Nr " + str(i))
#     print(records[i])
#     print(springs[i])
#     solutions.append(createCombos(springs[i], records[i]))
#     print(solutions[-1])

  
    
# print(sum(solutions))


# Part 2

springs = []
records = []
solutions = []

for line in lines:
    springs.append(re.findall(r'[.?#]', line))
    records.append(changeListDatatype(re.findall(r'\d+', line)))
    springs[-1] += "?"
    springs[-1] = springs[-1] * 5
    springs[-1] = springs[-1][:-1]
    records[-1] = records[-1] * 5


def combos2(sprngs, rules, i=0):
    # print(" ")
    # print(sprngs)
    sprID = []
    for s in getIt(sprngs):
        if s == i:
            sprID.append("_")
        else:
            sprID.append(" ")
    # print(sprID)
    # print(rules)
    if i >= len(sprngs):
        if not rules:
            # print("final1")
            # print(sprngs)
            return 1
        else:
            # print("error1")
            # print(sprngs)
            return 0
    if not rules:
        # print(sprngs[i:])
        if not "#" in sprngs[i:]:
            # print("final2")
            # print(sprngs)
            return 1
        else:
            # print("error2")
            # print(sprngs)
            return 0
        
    combos = 0
        
    if sprngs[i] in ("?", "."):
        # print("ADD 0")
        c0 = sprngs.copy()
        c0[i] = "0"
        combos += combos2(c0, rules, i+1)
    if sprngs[i] in ("?" "#"):
        # print("ADD 1")
        if (sum(rules) <= len(sprngs[i:])):
            if("." not in sprngs[i:i+rules[0]]):
                if(rules[0] == len(sprngs[i:]) or sprngs[i+rules[0]] != "#"):
                    c1 = sprngs.copy()
                    c1[i] = "1"
                    combos += combos2(c1, rules[1:], i+rules[0]+1)
        #         else:
        #             print("RULES DOESNT MATCH SPACE OR # AFTER RULE")
        #     else:
        #         print(". IN FOLLOWING SEQUENCES")
        # else:
            # print(sprngs[i])
            # print((sum(rules)))
            # print("NOT ENOUGH SPACE")
                
    return combos

for i in range(len(springs)):
# for i in range(5,6):
    print(" ")
    print("Nr " + str(i))
    # print(records[i])
    # print(springs[i])
    solutions.append(combos2(springs[i], records[i]))
    print(solutions[-1])
    
print(sum(solutions))