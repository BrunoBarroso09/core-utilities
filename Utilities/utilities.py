import os
import re
from dotenv import load_dotenv
from typing import Optional

#load_env outside the class because here load one time only
load_dotenv()

class Utilities:

    @staticmethod
    def mask_email(email: str) -> str:
        """
        Masks an email address for GDPR compliance.

        Args:
            email: The email address to mask.
        Returns:
            The masked email address.
        Raises:
            ValueError: If the email format is invalid.
        """
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email")
        user, domain = email.split('@', 1)
        domain, tld = domain.split('.', 1)
        masked_user = user[0] + '*' * len(user[1:])
        masked_domain = domain[0] + '*' * len(domain[1:])
        return f"{masked_user}@{masked_domain}.{tld}"

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate if the email format is valid
        
        Args:
            email: The email address to validate.
        Returns:
            True if the email format is valid, False otherwise.
        """
        if not email or '@' not in email:
            return False
        regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return bool(re.fullmatch(regex, email))

    @staticmethod
    def format_currency(value: float, symbol: str = '€') -> str:
        """
        Transform a number into a readable currency format

        Args:
            value: The value to format.
            symbol: The symbol to use.
        Returns:
            The formatted value.
        Raises:
            ValueError: If the value is not valid.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        return f"{value:,.2f} {symbol}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Read environment variable from .env file

        Args:
            key: Environment variable to read.
            default: Default value to return if key is not found.
        Returns:
            Environment variable value.
        """
        return os.getenv(key, default)

    @staticmethod
    def _validate_digit(digit: str) -> str:
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
        if not fiscal_number.isdigit() or len(fiscal_number) != 9:
            return False
        return fiscal_number[-1] == Utilities._validate_digit(fiscal_number[:8])

    @staticmethod
    def validate_postal_code(postal_code: str) -> bool:
        """
        Validate if the Portuguese postal code is valid

        Args:
            postal_code: The postal code to validate.
        Returns:
            True if the postal code is valid, False otherwise.
        """
        if not postal_code:
            return False
        regex_cp = r"\d{4}-\d{3}"
        return bool(re.fullmatch(regex_cp, postal_code))

    @staticmethod
    def _calculate_mod97(iban: str) -> int:
        """
        Private method to calculate the mod97 for the Portuguese IBAN.

        Args:
            iban: The IBAN to calculate the mod97 for.
        Returns:
            The mod97 calculated for the IBAN.
        """
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
        if not iban:
            return False
        iban = iban.replace(" ", "")
        if len(iban) != 25 or iban[:2] != "PT":
            return False
        if not iban[2:].isdigit():
            return False

        return Utilities._calculate_mod97(iban) == 1