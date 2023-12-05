# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:47:00 2022

@author: morit
"""

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



file1 = open('2.txt', 'r')
lines = file1.readlines()
opponentPlay = []
mePlay = []
playInstructions = []
playScores = []
outcomeScores = []

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
    if lines[i][0]=="A":
        opponentPlay.append(1)
    elif lines[i][0]=="B":
        opponentPlay.append(2)
    else:
        opponentPlay.append(3)
        
    if lines[i][2]=="X":
        mePlay.append(1)
    elif lines[i][2]=="Y":
        mePlay.append(2)
    else:
        mePlay.append(3)
        
    playInstructions.append(lines[i][2])



def outcome(opponent, me):
    if opponent == me:
        return 3
    elif me - (opponent % 3) == 1:
        return 6
    else:
        return 0
    
for i in range(len(mePlay)):
    playScores.append(mePlay[i])
    outcomeScores.append( outcome(opponentPlay[i], mePlay[i]))
    
finalScore = sum(playScores) + sum(outcomeScores)

# part 2
mePlay2 = []
playScores2 = []
outcomeScores2 = []

def decidePlay(opponent, instruction):
    plays = [3,1,2]
    if instruction == "X":
        return plays[(opponent + 2) % 3]
    elif instruction == "Y":
        return opponent
    else:
        return plays[(opponent + 1) % 3]
    
for i in range(len(opponentPlay)):
    mePlay2.append(decidePlay(opponentPlay[i], playInstructions[i]))
    playScores2.append(mePlay2[i])
    outcomeScores2.append( outcome(opponentPlay[i], mePlay2[i]))
    
finalScore2 = sum(playScores2) + sum(outcomeScores2)
