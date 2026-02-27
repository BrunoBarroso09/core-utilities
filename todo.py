# TODO: Validações Portuguesas
#  validate_phone_number — valida telemóvel português (9x, 2x)
#  validate_cc — valida Cartão de Cidadão
#  validate_niss — valida Número de Segurança Social
#  validate_license_plate — valida matrícula portuguesa (AA-00-AA)

# TODO: RGPD / Privacidade
#  mask_phone — 912345678 → 9*******8
#  mask_iban — PT50... → PT50 **** **** ****
#  mask_cc — mascara número do Cartão de Cidadão
#  mask_fiscal_number — 229007813 → 2*******3

# TODO: Formatações Portuguesas
#  format_phone_number — 912345678 → +351 912 345 678
#  format_fiscal_number — 229007813 → 229 007 813
#  format_postal_code — 1000001 → 1000-001
#  format_iban — PT50000201231234567890154 → PT50 0002 0123 1234 5678 9015 4

# TODO: Datas
#  validate_date — valida se uma data é válida
#  format_date_pt — 2026-02-24 → 24/02/2026
#  is_working_day — verifica se um dia é útil em Portugal (excluindo feriados)

# TODO: Strings
#  normalize_text — remove acentos (ção → cao)
#  truncate_string — corta string com limite de caracteres
#  sanitize_string — remove caracteres especiais