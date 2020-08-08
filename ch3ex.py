#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 06:12:07 2020

@author: rdrolis
"""

#Exercixe 3-1 Names
names = ['troy', 'dan', 'fred', 'shannon']
print(names)
print(names[0].title())
print(names[-1].title())
print(names[1].title())
print(names[2].title())
#Exercise 3-2 Greetings
message = f"\nHello {names[0].title()}, how have you been?"
print(message)
message = f"Hello {names[1].title()}, how have you been?"
print(message)
message = f"Hello {names[2].title()}, how have you been?"
print(message)
message = f"Hello {names[3].title()}, how have you been?"
print(message)
#Exercise 3-3 Your own list
transport = ['train', 'car', 'bus']
print(f"\nMy favorite mode of transportation is a bullet {transport[0]}")
print(f"I really don't like traveling by {transport[-1]}.")
print(f"The {transport[1]} I would love to drive is a Tesla.")
#Exercise 3-4 Guest List
guest = ['shim yi young', 'george patton', 'christy canyon']
print(f"\n{guest[0].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[1].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[2].title()} you are invited to dinner at my house tomorrow evening.")
#Exercise 3-5 Changing Guest list
guest_decline = guest.pop(0)
print(f"\n{guest_decline.title()} says they can't make it to dinner.")
guest.append('ava devine')
print(f"\n{guest[0].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[1].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[2].title()} you are invited to dinner at my house tomorrow evening.")
#Exercise 3-6 More Guests
guest.insert(0, 'amber lynn')
guest.insert(2, 'marilyn chambers')
guest.append('nina hartley')
print(guest)
print(f"\n{guest[0].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[1].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[2].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[3].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[4].title()} you are invited to dinner at my house tomorrow evening.")
print(f"{guest[5].title()} you are invited to dinner at my house tomorrow evening.")
#Exercise 3-7 Shrinking guest list
guest_notify=guest.pop(0)
print(f"\n{guest_notify.title()}, I am terribly sorry. I will have to cancel the invitation sent earlier.")
guest_notify=guest.pop(0)
print(f"{guest_notify.title()}, I am terribly sorry. I will have to cancel the invitation sent earlier.")
guest_notify=guest.pop(2)
print(f"{guest_notify.title()}, I am terribly sorry. I will have to cancel the invitation sent earlier.")
guest_notify=guest.pop(2)
print(f"{guest_notify.title()}, I am terribly sorry. I will have to cancel the invitation sent earlier.")
guest_notify=guest[0]
print(f"\n{guest_notify.title()} our dinner plans for tomorrow have been finalized")
guest_notify=guest[1]
print(f"{guest_notify.title()} our dinner plans for tomorrow have been finalized")
del guest[0]
del guest[0]
print(guest)
print()
#Exercise 3-8 Seeing the World
places = ['vatican city', 'reagan library', 'grand canyon', 'taj mahal']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
print()
#Exercise 3-9 Dinner Guests
guests = ['amber lynn', 'george patton', 'marilyn chambers', 'christy canyon', 'ava devine', 'nina hartley']
print(len(guests))
print(f"I have invited {len(guests)} guests for dinner tomorrow.")
print()
#Exercise 3-10 Every Function
states = ['oklahoma', 'iowa', 'texas' ]
print(states)
print(states[2].title())
print(states[0].title())
print(states[1].title())
message = f"I am from {states[-1].title()}."
print(message)
message = f"\nMy Mom was from {states[0].title()}."
print(message)
message = f"\n\tMy friend {names[2].title()} lives in {states[1].title()}."
print(message)
states.append('mississippi')
print(states)
states.insert(1, 'louisiana')
print(states)
print(states[3].title())
print(states[-1].title())
print(states[1].title())
print(states[0].title())
print(states[2].title())
states.pop(2)
print(states)
del states[3]
print(states)
