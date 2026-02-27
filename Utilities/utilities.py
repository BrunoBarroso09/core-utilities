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
        match indicative:
            case 241:
                return "Abrantes"
            case 235:
                return "Arganil"
            case 234:
                return "Aveiro"
            case 284:
                return "Beja"
            case 253:
                return "Braga"
            case 273:
                return "Bragança"
            case 262:
                return "Caldas da Rainha"
            case 272:
                return "Castelo Branco"
            case 286:
                return "Castro Verde"
            case 276:
                return "Chaves"
            case 239:
                return "Coimbra"
            case 275:
                return "Covilhã"
            case 268:
                return "Estremoz"
            case 266:
                return "Évora"
            case 289:
                return "Faro"
            case 233:
                return "Figueira da Foz"
            case 271:
                return "Guarda"
            case 277:
                return "Idanha-a-nova"
            case 244:
                return "Leiria"
            case 21:
                return "Lisboa"
            case 231:
                return "Mealhada"
            case 278:
                return "Mirandela"
            case 279:
                return "Moncorvo"
            case 285:
                return "Moura"
            case 283:
                return "Odemira"
            case 255:
                return "Penafiel"
            case 254:
                return "Peso da Régua"
            case 236:
                return "Pombal"
            case 242:
                return "Ponte de Sôr"
            case 245:
                return "Portalegre"
            case 282:
                return "Portimão"
            case 22:
                return "Porto"
            case 274:
                return "Proença-a-nova"
            case 243:
                return "Santarém"
            case 269:
                return "Santiago do Cacém"
            case 256:
                return "São João da Madeira"
            case 238:
                return "Seia"
            case 265:
                return "Setúbal"
            case 281:
                return "Tavira"
            case 249:
                return "Torres Novas"
            case 261:
                return "Torres Vedras"
            case 251:
                return "Valença"
            case 258:
                return "Viana do Castelo"
            case 263:
                return "Vila Franca de Xira"
            case 252:
                return "Vila Nova de Famalicão"
            case 259:
                return "Vila Real"
            case 232:
                return "Viseu"
            case 291:
                return "Funchal / Porto santo"
            case 295:
                return "Angra do Heroísmo / Graciosa / São Jorge"
            case 292:
                return "Corvo / Faial / Flores / Horta / Pico"
            case 296:
                return "Ponta Delgada / São Miguel / Santa Maria"
            case _:
                raise ValueError("Invalid indicative")

    @staticmethod
    def get_city_by_telephone(telephone: str) -> str:
        """
        Returns the city associated with the telephone prefix

        Args:
            telephone (str): Telephone number
        Returns:
            str: City associated with prefix
        Raises:
            ValueError: Invalid telephone number
        """
        if not telephone:
            raise ValueError("Invalid telephone number")
        if len(telephone) != 9:
            raise ValueError("The telephone number needs to be 9 digits")
        indicative = int(telephone[:2])
        if indicative == 21 or indicative == 22:
            return Utilities._get_city_by_indicative(int(telephone[:2]))
        return Utilities._get_city_by_indicative(int(telephone[:3]))