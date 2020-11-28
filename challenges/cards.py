#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:01:11 2020

@author: rrolison
"""

# Generate the suit of hearts in a deck of cards
# Chapter 4

hearts = []
clubs = []
diamonds = []
spades = []
deck = []
face = ['J', 'Q', 'K', 'A']

for n in range(2, 11):
    h = str(n) + " of Hearts"
    hearts.append(h)
    deck.append(h)

for f in face:
    h = f + " of Hearts"
    hearts.append(h)
    deck.append(h)

for n in range(2, 11):
    c = str(n) + " of Clubs"
    clubs.append(c)
    deck.append(c)

for f in face:
    c = f + " of Clubs"
    clubs.append(c)
    deck.append(c)

for n in range(2, 11):
    d = str(n) + " of Diamonds"
    diamonds.append(d)
    deck.append(d)

for f in face:
    d = f + " of Diamonds"
    diamonds.append(d)
    deck.append(d)

for n in range(2, 11):
    s = str(n) + " of Spades"
    spades.append(s)
    deck.append(s)

for f in face:
    s = f + " of Spades"
    spades.append(s)
    deck.append(s)

for card in deck:
    print(card)
print()
print(hearts)
print()
print(clubs)
print()
print(diamonds)
print()
print(spades)
print()
print(deck)
