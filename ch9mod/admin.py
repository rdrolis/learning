#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:56:13 2021

@author: rdrolis
"""

from user import User

"""Module to define admin user"""


class Admin(User):
    """Attributes specific to an administrative user."""

    def __init__(self, first, last, email, uname):
        """
        Initialize the attributes of the parent class
        Then initialize the the attributes specific to an admin user.
        """
        super().__init__(first, last, email, uname)
        self.privileges = Privileges()


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
