from .email import EmailUtilities
from .fiscal_number import FiscalNumberUtilities
from .iban import IBANUtilities
from .postal_code import PostalCodeUtilities
from .telephone import TelephonePrefixUtilities

mask_email = EmailUtilities.mask_email
validate_email = EmailUtilities.validate_email
validate_fiscal_number = FiscalNumberUtilities.validate_fiscal_number
validate_iban = IBANUtilities.validate_iban
validate_postal_code = PostalCodeUtilities.validate_postal_code
validate_telephone_number = TelephonePrefixUtilities.get_city_by_telephone