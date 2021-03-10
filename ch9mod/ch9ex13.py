#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:51:56 2021

@author: rdrolis
"""
import random


"""Module to simmulate rolling a die."""


class Die:
    """Model a die"""

    def __init__(self, sides=6):
        """Initialize a die that can be rolled"""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and number of sides"""
        return random.randint(1, self.sides)


# Roll the die 10 times and print the results
print("\nRolling the 6 sided die ten times.\nThe results are:")
d6 = Die()

results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print(results)
print("\nRolling the 10 sided die ten times.\nThe results are:")
d10 = Die(10)

results = []

for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print(results)
print("\nRolling the 20 sided die ten times.\nThe results are:")
d20 = Die(20)

results = []

for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print(results)
