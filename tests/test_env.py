from Utilities import Utilities

def test_env_is_valid(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "test_database_url")
    assert Utilities.get_env("DATABASE_URL") == "test_database_url"

def test_env_default_value(monkeypatch):
    assert Utilities.get_env("NON_EXISTENT", "default") == "default"

def test_env_default_none(monkeypatch):
    assert Utilities.get_env("NON_EXISTENT") is None

def test_env_is_empty(monkeypatch):
    monkeypatch.setenv("EMPTY_VAR", "")
    assert Utilities.get_env("EMPTY_VAR") == ""


def test_env_overwrite(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "old_value")
    monkeypatch.setenv("DATABASE_URL", "new_value")
    assert Utilities.get_env("DATABASE_URL") == "new_value"