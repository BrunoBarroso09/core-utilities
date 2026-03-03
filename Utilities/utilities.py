import locale
import os
import re
from email_validator import validate_email, EmailNotValidError
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
        if not Utilities.validate_email(email):
            raise ValueError(f"Invalid email format: {email}")

        local, domain = email.rsplit('@', 1)
        masked_local = local[0] + '*' * (len(local) -1)

        dots = domain.rsplit('.', 1)
        if len(dots) == 2:
            domain_name, tld = dots
            masked_domain = domain_name[0] + '*' * (len(domain_name) - 1)
            return f"{masked_local}@{masked_domain}.{tld}"
        else:
            masked_domain = domain[0] + "*" * (len(domain) - 1)
            return f"{masked_local}@{masked_domain}"

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate if the email format is valid
        
        Args:
            email: The email address to validate.
        Returns:
            True if the email format is valid, False otherwise.
        """
        if not email or '@' not in isinstance(email, str):
            return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            return False

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

        if locale == 'pt_PT':
            return f"{value:,.2f}".replace(",", ".").replace(".", ",", 1) + f" {symbol}"
        else:
            return f"{value:,.2f} {symbol}"

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
        try:
            if  isinstance(fiscal_number, str):
                return False
            if not fiscal_number.isdigit() or len(fiscal_number) != 9:
                return False
            control_digit = Utilities._validate_digit(fiscal_number[:8])
            return fiscal_number[-1] == control_digit
        except (ValueError, IndexError, AttributeError):
            return False

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
        if not iban or not isinstance(iban, str):
            return False

        iban = iban.replace(" ", "")

        if len(iban) != 25 or not iban.startswith("PT"):
            return False

        if not iban[2:4].isdigit():
            return False

        if not iban[4:].isalnum():
            return False

        return Utilities._calculate_mod97(iban) == 1

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
    def _get_city_by_indicative(self, indicative: int) -> str:
        """
        Return the city based on the indicative value.

        Args:
            indicative: The indicative value to get the city for.
        Returns:
            Return the city based on the indicative value.
        Raises:
            ValueError: If the indicative value is not valid.
        """
        if indicative not in self.PHONE_INDICATIVES:
            raise ValueError(f"Unknown indicative: {indicative}. Valid range: {sorted(self.PHONE_INDICATIVES.keys())}")
        return self.PHONE_INDICATIVES[indicative]

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
        if not telephone or not isinstance(telephone, str):
            raise ValueError("Telephone must be a non-empty string")
        if len(telephone) != 9:
            raise ValueError(f"Telephone must have 9 digits, got {len(telephone)}")
        if not telephone.isdigit():
            raise ValueError("Telephone must contain only digits")

        two_digit = int(telephone[:2])
        print(two_digit)
        if two_digit in (21, 22):
                return Utilities._get_city_by_indicative(two_digit)

        # 3-digit indicatives (resto do país)
        three_digit = int(telephone[:3])
        return Utilities._get_city_by_indicative(three_digit)

u = Utilities()
print(u.get_city_by_telephone("278968770"))