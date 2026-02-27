import os
import re
from dotenv import load_dotenv
from typing import Optional

#load_env outside the class because here load one time only
load_dotenv()

class Utilities:

    @staticmethod
    def mask_email(email: str) -> str:
        """Privacy: Transform email 'example@email.com' to 'e******@email.com'"""
        if not email or '@' not in email:
            return 'Invalid email'
        user, domain = email.split('@', 1)
        if '.' not in domain:
            return 'Invalid email'
        domain, tld = domain.split('.', 1)
        masked_user = user[0] + '*' * len(user[1:])
        masked_domain = domain[0] + '*' * len(domain[1:])
        return f"{masked_user}@{masked_domain}.{tld}"

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate if the email format is valid"""
        if not email or '@' not in email:
            return False
        regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return bool(re.fullmatch(regex, email))

    @staticmethod
    def format_currency(value: float, symbol: str = '€') -> str:
        """Transform a number into a readable currency format"""
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        return f"{value:,.2f} {symbol}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
        """Read environment variable from .env file"""
        return os.getenv(key, default)

    @staticmethod
    def _validate_digit(digit: str) -> str:
        """Private method to validate control digit for Portuguese fiscal number"""
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
        """Validate if the Portuguese fiscal number is valid"""
        if not fiscal_number.isdigit() or len(fiscal_number) != 9:
            return False
        return fiscal_number[-1] == Utilities._validate_digit(fiscal_number[:8])

    @staticmethod
    def validate_postal_code(postal_code: str) -> bool:
        """Validate if the Portuguese postal code is valid"""
        if not postal_code:
            return False
        regex_cp = r"\d{4}-\d{3}"
        return bool(re.fullmatch(regex_cp, postal_code))

    @staticmethod
    def _calculate_mod97(iban : str) -> int:
        """Private method to calculate the mod97 for the Portuguese IBAN"""
        code = iban[:4]
        digits = iban[4:]
        replace_code = code.replace("P", str(25)).replace("T", str(29))
        iban_formatted = digits + replace_code
        number = int(iban_formatted)
        result = number % 97
        return result

    @staticmethod
    def validate_iban(iban: str) -> bool:
        """Validate if the Portuguese IBAN is valid"""
        if not iban:
            return False
        iban = iban.replace(" ", "")
        if len(iban) != 25 or iban[:2] != "PT":
            return False
        if not iban[2:].isdigit():
            return False

        iban_valid = Utilities._calculate_mod97(iban)

        return iban_valid == 1