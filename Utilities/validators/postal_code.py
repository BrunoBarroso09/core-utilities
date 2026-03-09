import re

class PostalCodeUtilities:

    _CP_REGEX = re.compile(r'\d{4}-\d{3}$')
    @staticmethod
    def validate_postal_code(postal_code: str) -> bool:
        """
        Validate if the Portuguese postal code is valid

        Args:
            postal_code: The postal code to validate. EX: 1100-001
        Returns:
            True if the postal code is valid, False otherwise.
        """
        if not postal_code or not isinstance(postal_code, str):
            return False

        postal_code = postal_code.strip()
        return bool(PostalCodeUtilities._CP_REGEX.match(postal_code))