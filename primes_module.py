import math
from fast_modular_exponentiation import eulers_theorem

def exhaustive_fermat_primality_test(number):
    if number < 2:
        return False

    # As per the algorithm we know that we must first generate a list
    # of numbers from 2 ... number - 2. Note in python range is non-inclusive
    # of the final index hence we do number - 1.
    list_of_numbers = list(range(2, number - 1))
    
    for num in list_of_numbers:
        base = num
        exponent = number - 1
        modulo = number
        remainder = base ** exponent % modulo
        
        if remainder != 1:
            # We know that it is not a prime and hence we terminate the algorithm.
            return False
        
    return True

def sieve_of_eratosthenes(number):
    if number < 2:
        return []
    elif number == 2:
        return [2]
        
    # As per the algorithm we will firstly generate a list from 2 ... number.
    list_of_numbers = list(range(2, number + 1))

    # We know that the first entry will always be a prime i.e., 2.
    # We will remove every multiple of this entry from our list_of_numbers.
    # We will then do this repetitively until our next remaining prime
    # number is greater than the squareroot of our number.
    squareroot_of_number = math.floor(math.sqrt(number))
    temp_list = list_of_numbers.copy() # Bad as increasing space complexity. Will FIX.
    prime = list_of_numbers[0]
    prime_index = 0

    while True:
        for i in range(prime_index + 1, len(list_of_numbers)):
            if list_of_numbers[i] % prime == 0:
                # Then this number must be a multiple of our prime.
                # Hence remove it from our list.
                temp_list.remove(list_of_numbers[i])
        list_of_numbers = temp_list.copy()

        # As per the algorithm we know that the first remaining element in the list
        # will be the next prime. We then repeat the same mechanism of sieving.
        prime_index = prime_index + 1
        prime = temp_list[prime_index]

        if prime > squareroot_of_number:
            break
    
    return list_of_numbers

def main():
    #print("Upto what number would you like to generate the primes? ", end="")
    #number = int(input())
    #list_of_primes = sieve_of_eratosthenes(number)
    #print(f"The list of primes upto {number} are: {list_of_primes}")


    print("What number would you like to know is a prime or not? ", end="")
    number = int(input())
    is_prime = exhaustive_fermat_primality_test(number)
    print(f"Is it prime: {is_prime}")

if __name__ == "__main__":
    main()