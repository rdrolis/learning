#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:18:23 2020

@author: rdrolis
"""

# Generate deck of cards using nested loop

hearts = []
clubs = []
diamonds = []
spades = []
deck = []
face = ['J', 'Q', 'K', 'A']
num = range(2, 11)

# Generate Hearts and add to the deck

for n in num:
    h =  str(n) + ' of Hearts'
    hearts.append(h)
for f in face:
    h = f + ' of Hearts'
    hearts.append(h)

print(hearts)
deck.append(hearts)
print(deck)