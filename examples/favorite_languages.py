#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:48:23 2020

@author: rdrolis
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'javascript',
    'david': 'ruby',
    'jeff': 'groovy'
    }
lang = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {lang}.\n")

# Looping through dictionary
for n, la in favorite_languages.items():
    print(f"{n.title()}'s favorite language is {la.title()}.")
for n in favorite_languages.keys():
    print(n.title())
print()

# using a list as a condition while looping
friends = ['phil', 'sarah']
for n in favorite_languages.keys():
    print(f"Hi {n.title()}.")
    if n in friends:
        la = favorite_languages[n].title()
        print(f"\t {n.title()}, I see you like {la}")
if 'erin'not in favorite_languages.keys():
    print("Erin, please take our poll.")
print()

# Sort dictionary keys before looping
for n in sorted(favorite_languages.keys()):
    print(f"{n.title()}, thank you for taking our poll.")

# Loop through dictionary values
print("\nThe following languages have been mentioned:")
for la in favorite_languages.values():
    print(la.title())
print()

# Loop through dictionary for unique values and print them
for le in set(favorite_languages.values()):
    print(le.title())

# List within a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['javascript', 'haskell'],
    }
for n, l in favorite_languages.items():
    print(f"\n{n.title()}'s favorite languages are:")
    for la in l:
        print(f"\t{la.title()}")
print("hello world")
