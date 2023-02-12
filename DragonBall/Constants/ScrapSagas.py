class ScrapSagas:
    # these names have to be exactly the same as the asyde region

    sections = {
        "names": "Títulos",
        "data": "Datos",
        "serialization": "Serialización"
    }

    # font for character names section

    names = {
        "japan_name": "nombre-ja",
        "latin_name": "nombre-ja_latino",
    }

    # font for character data section

    data = {
        "episodes": "número de episodios (Anime)",
    }

    # font for serialization data section

    serialization = {
        "first_emision": "primera emisión",
        "last_emision": "última emisión",
    }

    # list of names to use according to sections

    list_character = {
        "names": list(names.values()),
        "data": list(data.values()),
        "serialization": list(serialization.values())
    }