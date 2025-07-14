import math
from sympy import isprime

number = -1

def unique_prime_factorisation(number):
    # Mathematically to optimise the algorithm we can divide the 'number' by upto it's squareroot of
    # the number itself i.e., √497 = 22.293496809607955 or taking it's ceiling we get 23.
    # So we divide 497 by all prime numbers from 1 to 23 inclusive to find it's unique prime factorisation.
    sqrt_of_num = math.ceil(math.sqrt(number))
    dict_of_prime_factors = {}
    list_of_corresponding_primes = [number] if isprime(number) else []

    for num in range(1, sqrt_of_num + 1):
        # The sympy library has this powerful 'isprime' function that utilises a very efficient algorithm
        # to find whether a number is prime or not. It has a time complexity of O((log n)³).
        if not isprime(num):
            continue
        
        while (True):
            if number % num == 0:
                # We have found the fact that the num | number i.e., the num divides number as hence
                # the number is divisible by the prime factor 'num'.
                number = number // num
                if num in dict_of_prime_factors:
                    dict_of_prime_factors[num] += 1
                else:
                    dict_of_prime_factors[num] = 1

                if number != 1:
                    list_of_corresponding_primes.append(number) 
                continue
            break
    
    for corresponding_prime in list_of_corresponding_primes:
        # We check if there is a corresponding prime number in the pair that is not included i.e.,
        # 497 has the prime factorisation of (7, 71). This algorithm will only find 7. We can divide
        # 497 by 7 and get 71. And we clearly see 71 is a prime so we append it to our results. We
        # already have that via 'number'.
        if isprime(corresponding_prime):
            if corresponding_prime not in dict_of_prime_factors:
                dict_of_prime_factors[corresponding_prime] = 1

    return dict_of_prime_factors

def calculate_totient(number):
    # We must first find the unique prime factorisation of this number.
    prime_factors = unique_prime_factorisation(number)

    # There are two ways to find the totient of a number.
    # Method 1:
    # We know that that totient of a prime number 'p' can be found as Φ(pᵏ) = pᵏ - pᵏ⁻¹.
    # We also know that Φ(mn) = Φ(m)Φ(n).
    totient = 1
    for prime in prime_factors:
        totient *= prime ** prime_factors[prime] - prime ** (prime_factors[prime] - 1)
    
    return totient