import math
from sympy import isprime
from totient_calculator import calculate_totient

def get_gcd(a, b):
    # To find the gcd of two numbers we can leverage the Euclidean Algorithm.
    gcd = -1
    while (True):
        quotient = a // b
        remainder = a - b * quotient
        #print(remainder)
        if remainder == 0:
            break
        
        a = b
        b = remainder
        gcd = remainder
        #print(gcd)
    return gcd

def eulers_theorem(base, exponent, modulo):
    """
    This function leverages Euler's Theorem. Euler's Therorem here is a fallback when
    the modulo passed in is NOT a prime. Recall that Euler's Theorem states,

    aᶲ(n) ≡ 1 (mod n).

    NOTE: We assume that gcd(a, n) = 1 from the main function.
    """
    
    # We first must calculate the totient of the modulo.
    totient = calculate_totient(modulo)
    outer_exponent = exponent // totient
    remainder = exponent - outer_exponent * totient

    # Now we must complete the part of the algorithm that will give us back the remainder
    # within the appropriate Z range.
    remaining_exponential = base ** remainder
    reducing_remaining_exponential = remaining_exponential // modulo
    new_remainder = remaining_exponential - reducing_remaining_exponential * modulo
    
    return new_remainder

def flt(base, exponent, modulo):
    """
    This function leverages Fermat's Little Theorem. We know that in order to leverage
    FLT that our modulo must be prime. So for any prime 'p' and any integer 'a', we know

    aᵖ ≡ a (mod p).

    Similarly, for any prime 'p' and any integer 'a' such that p ∤ a, we have that

    aᵖ⁻¹ ≡ 1 (mod p).
    """

    # We must first break up the exponent i.e., 12951 = 5 * 2590 + 1.
    # We can accomplish this by reducing the exponent.
    reduced_modulo = modulo - 1
    multiplier = exponent // reduced_modulo
    remainder = exponent - reduced_modulo * multiplier

    # Now if we had 268¹²⁹⁵¹ we can rewrite this as 268⁵*²⁹⁵⁰⁺¹ = (268²⁹⁵⁰)⁵ * 268.
    # FLT tells us that (268²⁹⁵⁰) ≡ 1 (mod 2591). We can rewrite it as (1)⁵ * 268.
    # This is just 268 (mod 2591).

    remaining_exponential = base ** remainder
    reducing_remaining_exponential = remaining_exponential // modulo
    new_remainder = remaining_exponential - reducing_remaining_exponential * modulo
    
    return new_remainder