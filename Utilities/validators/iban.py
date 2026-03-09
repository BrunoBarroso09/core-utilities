class IBANUtilities:

    @staticmethod
    def _calculate_mod97(iban: str) -> int:
        """
        Private method to calculate the mod97 for the Portuguese IBAN.

        Args:
            iban: The IBAN to calculate the mod97 for.
        Returns:
            The mod97 calculated for the IBAN.

        Algorithm:
            1. Move first 4 chars to end
            2. Replace letters: P=25, T=29
            3. Calculate mod 97 (valid = 1)
        """
        if not iban or not isinstance(iban, str) or len(iban) < 4:
            raise ValueError(f"Invalid IBAN")
        code = iban[:4]
        digits = iban[4:]
        replace_code = code.replace("P", "25").replace("T", "29")
        iban_formatted = digits + replace_code
        return int(iban_formatted) % 97

    @staticmethod
    def validate_iban(iban: str) -> bool:
        """
        Validate if the Portuguese IBAN is valid

        Args:
            iban: The IBAN to validate.
        Returns:
            True if the IBAN is valid, False otherwise.
        """
        if not iban or not isinstance(iban, str):
            return False

        iban = iban.strip().replace(" ", "")

        if len(iban) != 25 or not iban.startswith("PT"):
            return False

        if not iban[2:4].isdigit():
            return False

        if not iban[4:].isdigit():
            return False

        iban = iban.strip()
        try:
            mod97_result = IBANUtilities._calculate_mod97(iban)
            return mod97_result == 1
        except ValueError:
            return False