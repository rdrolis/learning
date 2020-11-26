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
    def __init__(self, first, last, email, uname):
        """Initialize user attributes"""
        self.first = first
        self.last = last
        self.email = email
        self.uname = uname
        
    def info(self):
        """Provide user info"""
        print(f"\nLast Name: {self.last.title()}")
        print(f"First Name: {self.first.title()}")
        print(f"Username: {self.uname}")
        print(f"Email address: {self.email}")
    def greet(self):
        print(f"\nHello {self.first.title()} {self.last.title()}, thank you \
for logging in.")


u1 = User('john', 'kelly', 'jkelly@cia.gov', 'jkelly')
u2 = User('santa', 'clause', 'santa@northpole.com', 'sclause')
u3 = User('jack', 'ryan', 'dci@cia.gov', 'jryan')

u1.info()
u1.greet()
u2.info()
u2.greet()
u3.info()
u3.greet()

    