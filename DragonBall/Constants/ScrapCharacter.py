class ScrapCharacter:
    # these names have to be exactly the same as the asyde region

    sections = {
        "names": "Nombres",
        "data": "Datos",
        "debut": "Debut"
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
        "birthday": "fecha de nacimiento",
        "deaths": "fecha de muerte",
        "age": "edad",
        "species": "raza",
        "occupation": "ocupación",
        "origin": "procedencia",
        "residence": "residencia",
        "transformations": "transformaciones",
        "fusion": "fusiones",
        "family": "familia",
        "affiliates": "afiliados"
    }

    # font for character debut section

    debut = {
        "sagas": "saga",
        "debut": "Primera aparición",
        "manga": "manga",
        "volume": "tomo",
        "anime": "anime",
        "introduction": "arco"
    }

    # list of names to use according to sections

    list_character = {
        "names": list(names.values()),
        "data": list(data.values()),
        "debut": list(debut.values())
    }
