#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:22:53 2020

@author: rrolison
"""

# Using Arbitrary Keyword arguments


def build_profile(first, last, **user_info):
    """Build a dictionary containing every thing we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
