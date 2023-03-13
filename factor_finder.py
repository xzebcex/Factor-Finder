# Factor Finder

# This program finds the factors of a given positive 
whole number.

import math
import sys

# A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

while True:  # Main loop program.
    response = input(
        'Enter a positive whole number to factor or [Q to QUIT]\n>')
    if response.upper() == 'Q':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of numbers.
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)

    # Convert to a set to get rid of duplicate factors.
    factors = list(set(factors))
    factors.sort()

    # Display the results.
    factors_str = [str(factor) for factor in factors]
    print(', '.join(factors_str))
