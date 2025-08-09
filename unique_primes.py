from totient_calculator import calculate_totient, unique_prime_factorisation

def main():
    print("What number would you prime factors of? ", end="")
    number = int(input())
    unique_primes = unique_prime_factorisation(number)

    for prime in unique_primes:
        print(f"{prime}, ", end="")

if __name__ == "__main__":
    main()