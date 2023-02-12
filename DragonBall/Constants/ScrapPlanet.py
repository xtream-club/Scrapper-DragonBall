class ScrapPlanet:
    # these names have to be exactly the same as the asyde region

    sections = {
        "names": "Nombres",
        "data": "Datos",
    }

    # font for character names section

    names = {
        "japan_name": "nombre-ja",
        "latin_name": "nombre-ja_latino",
    }

    # font for character data section

    data = {
        "localization": "localización",
        "gobernant": "gobernante",
        "residents": "residentes",
        "especies": "especie",
        "sagas": "saga",
        "debut": "aparición",
    }

    # list of names to use according to sections

    list_character = {
        "names": list(names.values()),
        "data": list(data.values())
    }