from totient_calculator import calculate_totient

def main():
    print("What number would you like to find the totient of? ", end="")
    number = int(input())
    print(calculate_totient(number))

if __name__ == "__main__":
    main()