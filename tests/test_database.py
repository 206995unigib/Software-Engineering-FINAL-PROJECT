# Tests for database.py. Run from the project root: python -m pytest -v
from database import add_vehicle, delete_vehicle, plate_exists


def test_add_vehicle():
    add_vehicle("TEST1", "Toyota", "Corolla", 2018, 20000, 20000)
    assert plate_exists("TEST1") == True
    delete_vehicle("TEST1")  # cleans up so app.db stays the same


def test_delete_vehicle():
    add_vehicle("TEST2", "Ford", "Fiesta", 2015, 9000, 80000)
    delete_vehicle("TEST2")
    assert plate_exists("TEST2") == False
