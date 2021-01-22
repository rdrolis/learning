#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:37:57 2020

@author: rdrolis
"""

# Exercise 9-1 Restaurant
# Exercise 9-4 add methods for number of customers served

class Restaurant:
    """Define a restaurant"""
    def __init__(self, n, c):
        """Initialize name and type"""
        self.n = n
        self.c = c
        self.nc = 0
    
    def desc(self):
        """Provide restaurant information"""
        print(f"{self.n.title()} serves {self.c} food.")
    
    def open(self):
        "State the restaurant is open"
        print(f"{self.n.title()} is open.")
    
    def cust(self):
        """Print a statement show number of customers served"""
        print(f"{self.n.title()} has served {self.nc} customers.")
    
    def set_cust(self, cu):
        """Set the number of customers served."""
        self.nc = cu
        
    def inc_cust(self, add):
        """Increment the number of customers served."""
        self.nc += add
        
        
r1 = Restaurant('applebees', 'casual')
r1.desc()
r1.open()
r1.cust()
r1.set_cust(1500)
r1.cust()
r1.inc_cust(2500)
r1.cust()

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
# Exercise 9-5 Add methods for numbeer of login attempts.

class User:
    """ Define user information"""
    def __init__(self, first, last, email, uname):
        """Initialize user attributes"""
        self.first = first
        self.last = last
        self.email = email
        self.uname = uname
        self.logins = 0
        
    def info(self):
        """Provide user info"""
        print(f"\nLast Name: {self.last.title()}")
        print(f"First Name: {self.first.title()}")
        print(f"Username: {self.uname}")
        print(f"Email address: {self.email}")
    def greet(self):
        print(f"\nHello {self.first.title()} {self.last.title()}, thank you \
for logging in.")
    def incr_login(self):
        """Increment the number of login attempts."""
        self.logins += 1
        print(f"You have logged in {self.logins} times.")
    def reset_login(self):
        self.logins = 0
        print(f"You have logged in {self.logins} times.")
        
        


u1 = User('john', 'kelly', 'jkelly@cia.gov', 'jkelly')
u2 = User('santa', 'clause', 'santa@northpole.com', 'sclause')
u3 = User('jack', 'ryan', 'dci@cia.gov', 'jryan')

u1.info()
u1.greet()
u2.info()
u2.greet()
u3.info()
u3.greet()
u1.greet()
u1.incr_login()
u1.greet()
u1.incr_login()
u1.greet()
u1.reset_login()

    