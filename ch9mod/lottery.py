#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:28:34 2021

@author: rrolison
"""

import string
from random import randint
from random import choice

# Generate possibilities list
poss = []

while len(poss) < 10:
    p = randint(1, 35)
    poss.append(p)

tr = 0

while tr < 5:
     tr = tr + 1
     l = choice(string.ascii_uppercase)
     poss.append(l)

# Exercise 9-14 Gernerate a winning ticket
print("\nFinding a winning ticket!!!")
win=[]
while len(win) < 4:
    pi = choice(poss)
    if pi not in win:
        print(f"We pulled a {pi}!")
        win.append(pi)

print(f"The winning ticket is: {win}")

# Exercise 9-15 Compare winning ticket to played ticket
print(f"\nExercise 9-15:\n")

def get_win(poss):
    """Return a winning ticket from the set of possibilities"""
    winner = []
    while len(winner) < 4:
        p = choice(poss)
        if p not in winner:
            winner.append(p)
    return winner

def get_play(poss):
    play = []
    while len(play) < 4:
        pl = choice(poss)
        if pl not in play:
            play.append(pl)
    return play

def check(play, winner):
    for e in play:
        if e not in winner:
            return False
        
    return True

wins = get_win(poss)
y = 0
max = 1000
won = False


while not won:
    new = get_play(poss)
    won = check(new, wins)
    y = y + 1
    if y >= max:
        break

if won: 
    print("There is a winner!")
    print(f"Your ticket: {new}")
    print(f"The winning ticket: {wins}")
    print(f"It only took {y} tries to win.")
else:
    print(f"The winning ticket: {wins}")
    print(f"Your ticket was: {new}")
    print(f"Tried {y} times without finding a winning ticket.")