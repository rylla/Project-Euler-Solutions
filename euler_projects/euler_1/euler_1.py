# Project Euler, Challenge 1.
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

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