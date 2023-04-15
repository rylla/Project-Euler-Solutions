# -----------------------------------

def get_divisors(input):
    
    # Mathematically a number is always divisible by itself and 1.
        # You can just append the values and save processing.
    # A number's divisor is never more than half of itself.
        # You only need to iterate half way.
    
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
    # Due to the commutiative law, you can simply use the smallest
    # known prime: 2. This reduces the complexity of the loop.

    # Take a number
        # Modulo by 'i', if not 0, increment until n 
        # If 0, store result
    # Take second value, do the same until no more division possible
    
    factors = []
    divisors = []
    i = 2
    while i <= input:
        if input % i == 0:
            factors.append(i)
            input /= i
            i = 1
        i += 1
        # divisors.append(i)
    return factors

# -----------------------------------
# Unit Tests

# Proving that the pFactors function returns valid data requires
    # that we loop through an arbitrary list of numbers, the product
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

# print(get_divisors(30))
print(get_pFactors(13195))
# print(get_pFactorsProof(2, 50))