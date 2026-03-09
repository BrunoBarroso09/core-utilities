import pytest
from Utilities.env import enviroment

class TestEnv:
    """Test suite for env() method"""

    def test_env_is_valid(self, monkeypatch):
        """Test env returns correct value."""
        monkeypatch.setenv("DATABASE_URL", "test_database_url")
        assert enviroment.EnvUtilities.get_env("DATABASE_URL") == "test_database_url"

    def test_env_default_value(self, monkeypatch):
        """Test env returns default value."""
        assert enviroment.EnvUtilities.get_env("NON_EXISTENT", "default") == "default"

    def test_env_default_none(self, monkeypatch):
        """Test env returns default is None."""
        assert enviroment.EnvUtilities.get_env("NON_EXISTENT") is None

    def test_env_is_empty(self, monkeypatch):
        """Test env returns empty string."""
        monkeypatch.setenv("EMPTY_VAR", "")
        assert enviroment.EnvUtilities.get_env("EMPTY_VAR") == ""

    def test_env_overwrite(self, monkeypatch):
        """Test env overwrites default value."""
        monkeypatch.setenv("DATABASE_URL", "old_value")
        monkeypatch.setenv("DATABASE_URL", "new_value")
        assert enviroment.EnvUtilities.get_env("DATABASE_URL") == "new_value"

    def test_env_invalid_type_int(self):
        """Test integer key raises TypeError."""
        with pytest.raises(TypeError):
            enviroment.EnvUtilities.get_env(123)

    def test_env_invalid_type_none(self):
        """Test None key raises TypeError."""
        with pytest.raises(TypeError):
            enviroment.EnvUtilities.get_env(None)

    def test_env_empty_key(self):
        """Test empty key raises ValueError."""
        with pytest.raises(ValueError):
            enviroment.EnvUtilities.get_env("")