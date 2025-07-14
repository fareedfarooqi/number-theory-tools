from totient_calculator import calculate_totient, unique_prime_factorisation

def main():
    print("What number would you prime factors of? ", end="")
    number = int(input())
    print(unique_prime_factorisation(number))

if __name__ == "__main__":
    main()