# Project Euler, Challenge 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# -----------------------------------

def get_divisors(input):
    
    # A number is always divisible by itself and 1.
        # You can just append the values and save processing.
    # A number's divisor is never more than half of itself.
        # (You only need to iterate half way).
    
    value = [1]
    i = 2
    while i <= (input / 2):
        if input % i == 0:
            value.append(i)
        i += 1
    value.append(input)
    return value

# -----------------------------------

def get_pFactors(input):
    
    # Each number should be split into two factors.
    # Each factor needs to be reduced until it's a prime number.
    # The easiest method is to try from smallest (2) to largest divisors,
    #   then, subdividing the result until you can no longer.
    
    factors = []
    i = 2
    while i <= input:
        if input % i == 0:
            factors.append(i)
            input /= i
            i = 1
        i += 1
    return factors

# -----------------------------------
# Unit Tests

# Proving that the pFactors function returns valid data requires
    # that we loop through an finite list of numbers, the product
    # of the result should equal the input.

def get_pFactorsProof(start, end):
    i = start
    val = 1
    while i < end:
        val = 1
        for x in get_pFactors(i):
            val *= x
        if val != i:
            print("\nError")
            print("Try:", i, "Function Result:", val)
            print(get_pFactors(i))
        else:
            print("\nTry:", i, "Function Result:", val)
            print(get_pFactors(i))
        i += 1

# -----------------------------------

# The output of get_pFactors() already returns a sorted list.
# To get the largest item, simply grab the last item in the list.

n = 600851475143
print("All prime factors of", n, ":", get_pFactors(n))
print("Largest prime factor of", n, ":", get_pFactors(n)[-1])