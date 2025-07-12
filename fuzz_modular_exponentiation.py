import sys
from sympy import isprime
from fast_modular_exponentiation import flt, eulers_theorem, get_gcd

def main():
    if len(sys.argv) != 4:
        print("Usage: fuzz_modular_exponentiation <base> <exponent> <modulo>", file=sys.stderr)
        sys.exit(1)

    base, exponent, modulo = map(int, sys.argv[1:])

    if get_gcd(base, modulo) != 1:
        sys.exit(0) # We skip as it is still valid. Our program hasn't crashed per se.

    if isprime(modulo):
        _ = flt(base, exponent, modulo)
    else:
        _ = eulers_theorem(base, exponent, modulo)

    sys.exit(0)
        
if __name__ == "__main__":
    main()