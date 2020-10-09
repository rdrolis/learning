# -*- coding: utf-8 -*-
plyrs = ['charles', 'martina', 'michael', 'florence', 'eli']
print(plyrs[0:3])
print(plyrs[1:4])
print(plyrs[:4])
print(plyrs[2:])
print()
print("Here are the first three players on my team:")
for p in plyrs[:3]:
    print(p.title())
