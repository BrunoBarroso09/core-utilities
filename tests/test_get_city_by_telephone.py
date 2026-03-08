import pytest
from Utilities import Utilities

class TestGetCityByTelephone:
    """Test suite for get_city_by_telephone() method"""

    def test_get_city_by_telephone_returns_str(self):
        """Test get_city_by_telephone returns string type."""
        result = Utilities.get_city_by_telephone("210455440")
        assert isinstance(result, str)

    def test_get_city_by_telephone_valid_braga(self):
        """Test get_city_by_telephone returns Braga for 253 area code."""
        result = Utilities.get_city_by_telephone("253455440")
        assert result == "Braga"

    def test_get_city_by_telephone_invalid_type_int(self):
        """Test get_city_by_telephone raises TypeError for integer input."""
        with pytest.raises(TypeError):
            Utilities.get_city_by_telephone(216455378)

    def test_get_city_by_telephone_empty_string(self):
        """Test get_city_by_telephone raises ValueError for empty string."""
        with pytest.raises(TypeError):
            Utilities.get_city_by_telephone("")

    def test_get_city_by_telephone_lisboa(self):
        """Test get_city_by_telephone returns Lisboa for 21 area code."""
        result = Utilities.get_city_by_telephone("210455440")
        assert result == "Lisboa"

    def test_get_city_by_telephone_porto(self):
        """Test get_city_by_telephone returns Porto for 22 area code."""
        result = Utilities.get_city_by_telephone("221212112")
        assert result == "Porto"

    def test_get_city_by_telephone_faro(self):
        """Test get_city_by_telephone returns Faro for 289 area code."""
        result = Utilities.get_city_by_telephone("289000000")
        assert result == "Faro"

    def test_get_city_by_telephone_too_short(self):
        """Test get_city_by_telephone raises ValueError for short phone."""
        with pytest.raises(TypeError):
            Utilities.get_city_by_telephone("289")

    def test_get_city_by_telephone_too_long(self):
        """Test get_city_by_telephone raises ValueError for long phone."""
        with pytest.raises(TypeError):
            Utilities.get_city_by_telephone("2890000000")

    def test_get_city_by_telephone_with_space(self):
        """Test get_city_by_telephone raises ValueError for space in phone."""
        with pytest.raises(TypeError):
            Utilities.get_city_by_telephone("25345 5440")

    def test_get_city_by_telephone_invalid_indicative(self):
        """Test get_city_by_telephone raises ValueError for invalid area code."""
        with pytest.raises(ValueError):
            Utilities.get_city_by_telephone("299212112")