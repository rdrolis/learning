#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:25:14 2020

@author: rdrolis
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

al_0 = {}
al_0['color'] = 'green'
al_0['points'] = 5
al_0['x_pos'] = 0
al_0['y_pos'] = 25
print(al_0)
al_0['color'] = 'yellow'
al_0['speed'] = 'medium'

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if al_0['speed'] == 'slow':
    x_increment = 1
elif al_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the x increment
al_0['x_pos'] = al_0['x_pos'] + x_increment
print(f"New position: {al_0['x_pos']}")
print(al_0)
del al_0['points']
print(al_0)
# print(al_0['points'])
point_value = al_0.get('points', 'No point value assigned.')
print(point_value)
