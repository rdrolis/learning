#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:59:26 2020

@author: rrolison
"""
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unc = ['alice', 'brian', 'candace']
conf = []
# Verify each user until there are no more unconfirmed users.
# Move each verfied user into the list of confirmed users.
while unc:
    cu = unc.pop()
    print(f"Verifiying user: {cu.title()}")
    conf.append(cu)
# Display all confirmed users
print("\nThe following users have been confirmed:")
for confu in conf:
    print(confu.title())
