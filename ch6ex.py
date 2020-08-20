#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:58:36 2020

@author: rdrolis
"""

#Exercise 6-1 Person
person={
        'last_name': 'rolison',
        'first_name': 'daryl',
        'age': 46,
        'city': 'san antonio'
        }
print(person['last_name'].title())
print(person['first_name'].title())
print(person['age'])
print(person['city'].title())
print()

#Exercise 6-2 Favorite Numbers
fav_num= {
    'joe': 6,
    'dan': 23,
    'bob': 5,
    'jessica': 7,
    'linda': 4,
    }
num = fav_num['joe']
print(f"Joe's favorite number is {num}.")
num = fav_num['dan']
print(f"Dan's favorite number is {num}.")
num = fav_num['bob']
print(f"Bob's favorite number is {num}.")
num = fav_num['jessica']
print(f"Jessica's favorite number is {num}.")
num = fav_num['linda']
print(f"Linda's favorite number is {num}.\n")

#Exercise 6-3 Glossary
gloss = {
    'list': 'A group of possible values for a variable.',
    'variable': 'An item to be defined by a string or an integer.',
    'integer': 'A whole number that can define a variable.',
    'float': 'A number containing one or more decimal places.',
    'conditional statement': 'A statement that defines conditions to be met \
before executing a task',
    'dictionary': 'A list of data containing keys and corresponding values.',
    'key': 'A pointer in a dictionary to a value.',
    'value': 'Data that defines a key in a dictionary.',
    }
term = gloss['variable']
print(f"Variable: {term}")
term = gloss['integer']
print(f"Integer: {term}")
term = gloss['float']
print(f"Float: {term}")
term = gloss['conditional statement']
print(f"Conditional Statement: {term}")
print()
#Exercise 6-4 Glossary 2
for g, v in gloss.items():
    print(f"{g.title()}: {v}")
print()
#Exercise 6-5 Rivers
rivers = {
    'han': 'south korea',
    'mississippi': 'united states',
    'rhein': 'germany',
    }
for r, c in rivers.items():
    print(f"The {r.title()} river is located in {c.title()}.")
print()
for r in rivers.keys():
    print(r.title())
print()
for c in rivers.values():
    print(c.title())
#Exercise 6-6 Polling

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'javascript',
    'david': 'ruby',
    'jeff': 'groovy'
    }
poll = ['tim', 'mary', 'edward', 'carena', 'larry', 'jen']
for n in poll:
    if n in fav_lang.keys():
        print(f"{n.title()} thank you for taking our poll.")
    elif n not in fav_lang.keys():
        print(f"{n.title()}, please take our favorite languages poll.")

    