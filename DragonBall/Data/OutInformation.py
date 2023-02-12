import json


class OutInformation:
    RESOURCE_NOT_FOUND = 'Not Found In Web'

    @staticmethod
    def beautiful_print_dict(json_dict: dict):
        beautiful_print = json.dumps(json_dict, indent=4, ensure_ascii=False).encode('utf-8')
        return beautiful_print.decode('utf-8')

    @classmethod
    def clean_not_found_scrape(cls, character: dict):
        for key, value in character.copy().items():
            if value == cls.RESOURCE_NOT_FOUND:
                character.pop(key)
            elif isinstance(value, dict):
                cls.clean_not_found_scrape(value)
        return character
