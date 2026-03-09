class TelephonePrefixUtilities:

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

        if indicative not in TelephonePrefixUtilities.PHONE_INDICATIVES:
            raise ValueError(f"Unknown indicative: {indicative}")

        return TelephonePrefixUtilities.PHONE_INDICATIVES[indicative]

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
            raise TypeError(f"Telephone must have 9 digits, got {len(telephone)}")

        if not telephone.isdigit():
            raise TypeError("Telephone must contain only digits")

        telephone = telephone.strip()
        two_digit = int(telephone[:2])
        three_digit = int(telephone[:3])

        if two_digit in (21, 22):
            return TelephonePrefixUtilities._get_city_by_indicative(two_digit)
        elif three_digit in TelephonePrefixUtilities.PHONE_INDICATIVES:
            return TelephonePrefixUtilities._get_city_by_indicative(three_digit)
        else:
            raise ValueError("Invalid telephone indicative")