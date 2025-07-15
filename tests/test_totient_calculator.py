import pytest
from totient_calculator import unique_prime_factorisation, calculate_totient

# This is our happy-path test.
@pytest.mark.parametrize("num,expected", [
    (1, {}),
    (10, {2: 1, 5: 1}),
    (17, {17: 1}),
    (63, {3: 2, 7: 1}),
    (483, {3: 1, 7: 1, 23: 1}),
    (913, {11: 1, 83: 1}),
    (9273, {3: 1, 11: 1, 281: 1}),
    (175230317, {13037: 1, 13441: 1}),
])

def test_unique_prime_factorisation(num, expected):
    assert unique_prime_factorisation(num) == expected

@pytest.mark.parametrize("bad_num", [0, -10, -123])
def test_unique_prime_factorisation_rejects_non_positive(bad_num):
    with pytest.raises(ValueError) as excinfo:
        unique_prime_factorisation(bad_num)
    
    assert "Number must be a positive number, you passed" in str(excinfo)

@pytest.mark.parametrize("bad_input", ["sam", 10.23, None])
def test_unique_prime_factorisation_rejects_non_integer(bad_input):
    with pytest.raises(TypeError) as excinfo:
        unique_prime_factorisation(bad_input)
    
    assert "is not of a type 'int'!" in str(excinfo)