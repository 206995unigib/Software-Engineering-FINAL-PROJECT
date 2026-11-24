# Tests for validation.py. Run from the project root: python -m pytest -v
from validation import validate_vehicle


def test_valid_vehicle():
    assert validate_vehicle("AB0213", "2020", "15000", "30000") == True


def test_valid_plate():
    assert validate_vehicle("", "2020", "15000", "30000") == 'Plate cannot be empty'


def test_valid_year():
    assert validate_vehicle("AB0213", "20201", "15000", "30000") == "Year must be between 1930 & 2026"


def test_valid_price():
    assert validate_vehicle("AB0213", "2020", "-25", "30000") == "Price must be between 0 & 10000000"


def test_valid_kms():
    assert validate_vehicle("AB0213", "2020", "15000", "3000000") == "Kms must be between 0 and 500000"


def test_letters_instead_of_numbers():
    assert validate_vehicle("AB0213", "abc", "15000", "30000") == "Year, price and KMs must be numbers"
