import pytest
from totient_calculator import unique_prime_factorisation, calculate_totient

@pytest.mark.parametrize("num,expected", [
    (483, {3: 1, 7: 1, 23: 1})
])

def test_unique_prime_factorisation(num, expected):
    assert unique_prime_factorisation(num) == expected