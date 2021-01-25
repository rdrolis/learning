#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:44:10 2021

@author: rdrolis
"""

""" Modules for User, Admin, and Privileges"""


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


class Privileges:
    """Initialize the privileges for an admin user"""

    def __init__(self, privileges=[]):
        """Initialize the privileges"""
        self.privileges = privileges

    def show_privilege(self):
        print("You have the following privileges:")
        if self.privileges:
            for pr in self.privileges:
                print(f"-{pr}")
        else:
            print("This user has no privileges.")


class Admin(User):
    """Attributes specific to an administrative user."""

    def __init__(self, first, last, email, uname):
        """
        Initialize the attributes of the parent class
        Then initialize the the attributes specific to an admin user.
        """
        super().__init__(first, last, email, uname)
        self.privileges = Privileges()
