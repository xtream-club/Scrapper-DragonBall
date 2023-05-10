Scrapper-DragonBall
===============
Scrapper unofficial de Dragon Ball inspirado en su fandom. <https://dragonball.fandom.com/es/wiki/Dragon_Ball_Wiki_Hispano>. Esta api nos permite obtener datos de personajes, sagas, fusiones, lugares y videojuegos de manera sencilla. Para poder utilizarlo en nuestras aplicaciones.

Requerimientos
============
Para instalar los requerimientos instale los requerimientos del archivo requirements.txt con el siguiente comando

    pip install -r requirement.txt

Importaciones
============

    from DragonBall.Data.Characters import Characters
    from DragonBall.Data.Sagas import Sagas
    from DragonBall.Data.Planets import Planets
    from DragonBall.Data.Fusions import Fusions
    from DragonBall.Data.VideoGames import VideoGames
    from DragonBall.Data.OutInformation import OutInformation

Instalación
============

    pip install Dragon-Ball-API

Usage
=====

    >>> from DragonBall.Data.Characters import Characters
    
    >>> search_goku = Characters('Goku')
    >>> search_goku.character_information()
    
    {
    'name': 'Son Goku', 'image': 'https://example.com', 'description': 'descripcion', 
    'names': {'japan_name': '...', 'latin_name': '...', 'pronunciation_name': '...', 'other_names': '...'}, 
    'data': {'gender': '...', 'birthday': '...', 'origin': '...', 'family': ['...','...'], 'transformations': ['...', '...'], etc.. },
    'debut': {'sagas': [{'title': '...', 'url': '...'}], 'debut': '...'}
    }
    

Algunos personajes tendran más datos que otros. Eso dependera de la información que se encuentre en la wiki de dragon ball en ese momento. Si deseamos podemos pasar una lista de personajes a buscar y usar el método list para devolvernos la información de todos los personajes.

    >>> from DragonBall.Data.Characters import Characters
    
    goku_family = ['Son Gohan (abuelo)', 'Bardock', 'Gine', 'Raditz', 'Rey Gyuma', 'Milk', 'Gohan', 'Goten', 'Mr. Satán', 'Videl', 'Pan', 'Son Goku Jr.']
    
    >>> character_list = Characters.character_list(goku_family)
    
    [{'...'},{'...'}]

   


Podemos ver una lista de los personajes usando el método list de la clase. De la siguiente manera.



    >>> Characters.list()
    
    {
    'Personajes por raza': ['Androides', 'Animales', 'Arlianos', 'Ángeles', '...', '...'],
    'Personajes por asociación': ['...', '...', '...']
    }



Si queremos imprimir los datos de manera más legible podemos utilizar el método beautiful_print_dict de la clase OutInformation


    >>> OutInformation.beautiful_print_dict(Characters.list())
    
    "Personajes por raza": [
        "Androides",
        "Animales",
        "Arlianos",
        "Ángeles",
        "..."
     ]
     


Todos estos metodos los podemos aplicar en todas sus clases (sagas, juegos, etc).
