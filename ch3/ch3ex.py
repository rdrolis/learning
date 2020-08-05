#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:12:07 2020

@author: rdrolis
"""

#Exercixe 3-1 Names
names = ['troy', 'dan', 'fred', 'shannon']
print(names)
print(names[0].title())
print(names[-1].title())
print(names[1].title())
print(names[2].title())
#Exercise 3-2 Greetings
message = f"\nHello {names[0].title()}, how have you been?"
print(message)
message = f"Hello {names[1].title()}, how have you been?"
print(message)
message = f"Hello {names[2].title()}, how have you been?"
print(message)
message = f"Hello {names[3].title()}, how have you been?"
print(message)
#Exercise 3-3 Your own list
transport = ['train', 'car', 'bus']
print(f"\nMy favorite mode of transportation is a bullet {transport[0]}")
print(f"I really don't like traveling by {transport[-1]}.")
print(f"The {transport[1]} I would love to drive is a Tesla.")


