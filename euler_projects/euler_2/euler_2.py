# By considering the terms in the Fibonacci sequence whose 
#    values do not exceed four million, find the sum of the 
#    even-valued terms.
# Project Euler considers the first ten in the series: 
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# The first 10 can also be:
#    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Wolfram Alpha defines Fib(10) as 55.
# We will be using Euler's definition.

a = 0
b = 1
sum = 0

fib = []
fibEven = []
# Uncomment below for 0 leading sequence
# fib.append(a)
# fib.append(b)

max = 4000000
while b <= max:
    a += b
    b += a
    if not a >= max:
        fib.append(a)
        if a % 2 == 0:
            fibEven.append(a)
    if not b >= max:
        fib.append(b)
        if b % 2 == 0:
            fibEven.append(b)

for i in fibEven:
    sum += i
    
print("All Fibonacci numbers in sequence:", fib, "\n")
print("All even Fibonacci numbers in sequence:", fibEven, "\n")
print("Sum of even:", sum, "\n")