#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:37:57 2020

@author: rdrolis
"""

# Exercise 9-1 Restaurant

class Restaurant:
    """Define a restaurant"""
    def __init__(self, n, c):
        """Initialize name and type"""
        self.n = n
        self.c = c
    
    def desc(self):
        """Provide restaurant information"""
        print(f"{self.n.title()} serves {self.c} food.")
    
    def open(self):
        "State the restaurant is open"
        print(f"{self.n.title()} is open.")
        
r1 = Restaurant('applebees', 'casual')
r1.desc()
r1.open()

# Exercise 9-2 Three Restaurants

r2 = Restaurant('whataburger', 'fast')
r3 = Restaurant('olive garden', 'italian casual')
r4 = Restaurant('pappadeaux', 'Louisiana coast')
print()
r2.desc()
r2.open()
print()
r3.desc()
r3.open()
print()
r4.desc()
r4.open()

# Exercise 9-3 Users

class User:
    """ Define user information"""
    def __init__(self, first, last, email, ):
        """Initialize user attributes"""
        self.first = first
        self.last = last
    
    def 