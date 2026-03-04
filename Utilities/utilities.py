import os
import re
from babel.numbers import format_currency
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
        if not email or '@' not in email or '.' not in email:
            raise ValueError(f"Invalid email: {email}")

        local, domain = email.rsplit('@', 1)

        if len(local) == 1:
            masked_local = '*'
        else:
            masked_local = local[0] + '*' * (len(local) - 1)

        domain_name, tld = domain.rsplit('.', 1)

        if len(domain_name) == 1:
            masked_domain = '*'
        else:
            masked_domain = domain_name[0] + '*' * (len(domain_name) - 1)

        return f"{masked_local}@{masked_domain}.{tld}"

    _EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate if the email format is valid

        Args:
            email: The email address to validate.
        Returns:
            True if the email format is valid, False otherwise.
        """
        if not isinstance(email, str):
            return False

        if not email or '@' not in email:
            return False

        email = email.strip()

        return bool(Utilities._EMAIL_REGEX.search(email))

    @staticmethod
    def format_currency(value: float) -> str:

        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value")

        return format_currency(value, 'EUR')

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
        if not key or isinstance(key, str):
            raise ValueError("Key must be non-empty string")

        key = key.strip()
        value = os.getenv(key)
        if value == default:
            return f"Environment variable '{key}' not found, using default"
        else:
            return value

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
            expected_digit = Utilities._calculate_check_digit(fiscal_number[:8])
            return fiscal_number[-1] == expected_digit
        except (ValueError, IndexError, AttributeError):
            return False

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
        return bool(Utilities._CP_REGEX.match(postal_code))

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
            mod97_result = Utilities._calculate_mod97(iban)
            return mod97_result == 1
        except ValueError:
            return False

    PHONE_INDICATIVES = {
        241: "Abrantes",
        235: "Arganil",
        234: "Aveiro",
        284: "Beja",
        253: "Braga",
        273: "Bragança",
        262: "Caldas da Rainha",
        272: "Castelo Branco",
        286: "Castro Verde",
        276: "Chaves",
        239: "Coimbra",
        275: "Covilhã",
        268: "Estremoz",
        266: "Évora",
        289: "Faro",
        233: "Figueira da Foz",
        271: "Guarda",
        277: "Idanha-a-nova",
        244: "Leiria",
        21: "Lisboa",
        231: "Mealhada",
        278: "Mirandela",
        279: "Moncorvo",
        285: "Moura",
        283: "Odemira",
        255: "Penafiel",
        254: "Peso da Régua",
        236: "Pombal",
        242: "Ponte de Sôr",
        245: "Portalegre",
        282: "Portimão",
        22: "Porto",
        274: "Proença-a-nova",
        243: "Santarém",
        269: "Santiago do Cacém",
        256: "São João da Madeira",
        238: "Seia",
        265: "Setúbal",
        281: "Tavira",
        249: "Torres Novas",
        261: "Torres Vedras",
        251: "Valença",
        258: "Viana do Castelo",
        263: "Vila Franca de Xira",
        252: "Vila Nova de Famalicão",
        259: "Vila Real",
        232: "Viseu",
        291: "Funchal / Porto santo",
        295: "Angra do Heroísmo / Graciosa / São Jorge",
        292: "Corvo / Faial / Flores / Horta / Pico",
        296: "Ponta Delgada / São Miguel / Santa Maria",
    }
    @staticmethod
    def _get_city_by_indicative(indicative: int) -> str:
        """
        Return the city based on the indicative value.

        Args:
            indicative: The indicative value to get the city for.
        Returns:
            Return the city based on the indicative value.
        Raises:
            ValueError: If the indicative value is not valid.
        """
        if not isinstance(indicative, int):
            raise TypeError(f"Indicative must be integer")

        if indicative not in Utilities.PHONE_INDICATIVES:
            raise ValueError(f"Unknown indicative: {indicative}")

        return Utilities.PHONE_INDICATIVES[indicative]

    @staticmethod
    def get_city_by_telephone(telephone: str) -> str:
        """
        Returns the city associated with the telephone prefix.

        Portuguese telephone format:
        - 2-digit prefix: Lisboa (21), Porto (22)
        - 3-digit prefix: All other cities

        Args:
            telephone: 9-digit telephone number
        Returns:
            City name
        Raises:
            ValueError: Invalid telephone format
        """
        if not isinstance(telephone, str):
            raise TypeError(f"Telephone must be string")

        telephone = telephone.strip()

        if len(telephone) != 9:
            return f"Telephone must have 9 digits, got {len(telephone)}"

        if not telephone.isdigit():
            return "Telephone must contain only digits"

        telephone = telephone.strip()
        two_digit = int(telephone[:2])

        if two_digit in (21, 22):
            return Utilities._get_city_by_indicative(two_digit)

        three_digit = int(telephone[:3])
        return Utilities._get_city_by_indicative(three_digit)