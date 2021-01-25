#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:48:15 2021

@author: rdrolis
"""

from users import User, Admin, Privileges

u1 = User('jack', 'ryan', 'dci@cia.gov', 'jryan')
u1.info()
u1 = Admin('jack', 'ryan', 'dci@cia.gov', 'jryan')
u1.greet()
u1.privileges.show_privilege()
print("Adding admin privileges...")
u1_privileges = [
    'can add users',
    'can delete users',
    'can moderate discussions',
    ]
u1.privileges.privileges = u1_privileges
u1.privileges.show_privilege()
