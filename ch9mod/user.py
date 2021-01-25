#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:54:57 2021

@author: rdrolis
"""

"""Module to define user attributes"""


class User:
    """ Define user information"""

    def __init__(self, first, last, email, uname):
        """Initialize user attributes"""
        self.first = first.title()
        self.last = last.title()
        self.email = email
        self.uname = uname
        self.logins = 0

    def info(self):
        """Provide user info"""
        print(f"\n{self.first} {self.last}")
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
