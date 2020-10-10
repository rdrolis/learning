#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:34:23 2020

@author: rrolison
"""

al_0 = {'color': 'green', 'points': 5}
al_1 = {'color': 'yellow', 'points': 10}
al_2 = {'color': 'red', 'points': 15}
aliens = [al_0, al_1, al_2]
for a in aliens:
    print(a)
print()
# Make 30 green aliens
aliens = []
for al_num in range(30):
    new_al = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_al)
for al in aliens[:5]:
    print(al)
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)} ")
print()
# Change the first three aliens to yellow
for al in aliens[:3]:
    if al['color'] == 'green':
        al['color'] = 'yellow'
        al['speed'] = 'medium'
        al['points'] = 10
# print the first 5 aliens
for al in aliens[:5]:
    print(al)
