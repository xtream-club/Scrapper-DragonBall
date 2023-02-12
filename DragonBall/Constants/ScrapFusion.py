class ScrapFusion:
    # these names have to be exactly the same as the asyde region

    sections = {
        "names": "Nombres",
        "data": "Otros datos",
    }

    # font for character names section

    names = {
        "japan_name": "nombre-ja",
        "latin_name": "nombre-ja_latino",
        "pronunciation_name": "pronunciación",
        "other_names": "otros nombres"
    }

    # font for character data section

    data = {
        "gender": "sexo",
        "date of origin": "fecha de origen",
        "species": "raza",
        "fusion": "fusionados",
        "method_used": "método",
        "transformations": "transformaciones",
        "apparition": "aparición",
        "debut": "Primera aparición"
    }

    # list of names to use according to sections

    list_character = {
        "names": list(names.values()),
        "data": list(data.values()),
    }
