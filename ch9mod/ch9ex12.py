#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:00:39 2021

@author: rdrolis
"""

from user import User
from admin import Admin

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
print(f"\n Admin user: {u1.uname}")
u1.privileges.show_privilege()
