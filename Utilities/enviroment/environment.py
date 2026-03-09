from typing import Optional
import os
from dotenv import load_dotenv

#load_env outside the class because here load one time only
load_dotenv()

class EnvUtilities:

    @staticmethod
    def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Read environment variable from .environment file

        Args:
            key: Environment variable to read.
            default: Default value to return if key is not found.
        Returns:
            Environment variable value.
        """
        if not isinstance(key, str):
            raise TypeError(f"Key must be string, got {type(key).__name__}")

        if not key or not key.strip():
            raise ValueError("Key must be non-empty string")

        key = key.strip()
        value = os.getenv(key, default)

        return value