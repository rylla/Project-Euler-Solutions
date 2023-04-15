# Project Euler, Challenge 1.
# Get multiples of 3 and 5 within range of numbers.
# This also stores the multiples in a list and prints them.

multiples = []
sum = 0
for i in range(10):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        multiples.append(i)
print("Multiples:", multiples)
print("Sum:", sum)