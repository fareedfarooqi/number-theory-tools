import random
import math
from sympy import isprime

def generate_random_prime():
    return random.randint(1,100)

print(generate_random_prime())