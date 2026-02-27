import pytest

from Utilities import Utilities

def test_get_city_by_telephone_lisbon():
    result = Utilities.get_city_by_telephone("210455440")
    assert result == "Lisboa"

def test_get_city_by_telephone_telephone_Porto():
    result = Utilities.get_city_by_telephone("221212112")
    assert result == "Porto"

def test_get_city_by_telephone_telephone_Faro():
    result = Utilities.get_city_by_telephone("289000000")
    assert result == "Faro"

def test_get_city_by_telephone_telephone_invalid():
    with pytest.raises(ValueError):
        Utilities.get_city_by_telephone("212")

def test_get_city_by_telephone_telephone_empty():
    with pytest.raises(ValueError):
        Utilities.get_city_by_telephone("")

def test_get_city_by_telephone_telephone_invalid_indicative():
    with pytest.raises(ValueError):
        Utilities.get_city_by_telephone("299212112")
