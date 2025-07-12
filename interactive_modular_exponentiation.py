from sympy import isprime
from fast_modular_exponentiation import get_gcd, flt, eulers_theorem

while (True):
    print("To find the residue of a number, please input the following:")
    print("Base: ", end="")
    base = int(input())

    print("Exponent: ", end="")
    exponent = int(input())

    print("Modulo: ", end="")
    modulo = int(input())

    # Base and modulus must be coprime in order for us to find a valid residue.
    if get_gcd(base, modulo) != 1:
        print(f"The GCD of the base and modulus must be 1! Try again.")
        continue

    if isprime(modulo):
        # If the modulus is a prime we can apply an optimisation i.e., we can
        # leverage Fermat's Little Theorem to quickly find the residue.
        print(flt(base, exponent, modulo))
    else:
        print(eulers_theorem(base, exponent, modulo))