#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:12:54 2020

@author: rrolison
"""

rs = {}

# Set a flag to indicate polling is active.
poll_act = True

while poll_act:
    # Prompt for the persons' name and response
    n = input("\nWhat is your name? ")
    r = input("\nWhat mountain would you like to climb today? ")

    # Store the response in the dictionary.
    rs[n] = r

    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        poll_act = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for n, r in rs.items():
    print(f"{n.title()} would like to climb {r.title()}.")
