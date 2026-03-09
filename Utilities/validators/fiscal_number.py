class FiscalNumberUtilities:

    @staticmethod
    def _calculate_check_digit(digit: str) -> str:
        """
        Private method to validate control digit for Portuguese fiscal number

        Args:
            digit: The control digit to validate.
        Returns:
            The validated control digit.
        Raises:
            ValueError: If the control digit is not valid.
        """
        if not digit.isdigit() or len(digit) != 8:
            raise ValueError("All characters need to be digits and length must be 8")
        sum_digit = (
                int(digit[0]) * 9 + int(digit[1]) * 8 + int(digit[2]) * 7 +
                int(digit[3]) * 6 + int(digit[4]) * 5 + int(digit[5]) * 4 +
                int(digit[6]) * 3 + int(digit[7]) * 2
        )
        rest = sum_digit % 11
        return "0" if rest < 2 else str(11 - rest)

    @staticmethod
    def validate_fiscal_number(fiscal_number: str) -> bool:
        """
        Validate if the Portuguese fiscal number is valid

        Args:
            fiscal_number: The fiscal number to validate.
        Returns:
            True if the fiscal number is valid, False otherwise.
        """
        if not isinstance(fiscal_number, str) or not fiscal_number.isdigit() or len(fiscal_number) != 9:
            return False

        fiscal_number = fiscal_number.strip()

        try:
            expected_digit = FiscalNumberUtilities._calculate_check_digit(fiscal_number[:8])
            return fiscal_number[-1] == expected_digit
        except (ValueError, IndexError, AttributeError):
            return False