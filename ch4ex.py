# -*- coding: utf-8 -*-
# Exercise 4-1 Pizzas
pizzas = ['pepperoni', 'combination', 'cheese', 'sausage']
for pizza in pizzas:
    print(pizza)
print()
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("Pizza is one of my favorites.\n")

# Exercise 4-2 Animals
reptiles = ['snake', 'lizard', 'alligator']
for reptile in reptiles:
    print(f"A {reptile} is a reptile.")
print("These are all examples of reptiles.")

# Exercise 4-3 Counting to Twenty
count = list(range(1, 21))
print(count)

# Exercise 4-4 Million
mil = list(range(1, 1000001))
# for m in mil:
# print(m)

# Exercise 4-5 Summing a million
print(max(mil))
print(min(mil))
print(sum(mil))
print()

# Exercise 4-6 Odd numbers
for odd in range(1, 20, 2):
    print(odd)
print()

# Exercise 4-7 Threes
for t in range(3, 31, 3):
    print(t)
print()

# Exercise 4-8 Cubes
cu = []
for c in range(1, 11):
    cu.append(c**3)
print(cu)
cu = []

print()
# Exercise 4-9 Cubes List Comprehension
cu = [c**3 for c in range(1, 11)]
print(cu)

# Exercise 4-10 Slices
pizzas.append('spinach')
print("\nThe first three items in the list are:")
print(pizzas[:3])
print("\nThe second three items in the list are:")
print(pizzas[1:4])
print("\nThe last three items in the list are:")
print(pizzas[2:5])

# Exercise 4-11
pz = pizzas[:]
fp = pizzas[:]
pz.append('dessert')
fp.append('alfredo')
print(pz)
print(fp)

# Exercise 4-12 More Loops
mf = ['chili', 'steak', 'bbq']
ff = mf[:]
mf.append('ice cream')
ff.append('meat loaf')
print("\nMy favorite foods are:")
for m in mf:
    print(m.title())
print("\nMy friend's favorite foods are:")
for f in ff:
    print(f.title())
print()

# Exercise 4-13 Buffet
menu = ('meat loaf', 'prime rib', 'fried chicken', 'green beans', 'potatoes')
for m in menu:
    print(m)
# menu[1] = 'catfish'
menu = ('catfish', 'prime rib', 'hushpuppies', 'green beans', 'potatoes')
print()
for m in menu:
    print(m)

# Exercise 4-14 and 4-15 Code Review
