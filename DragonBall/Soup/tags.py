from bs4 import BeautifulSoup

from DragonBall.Constants.URLS import URL
from DragonBall.Data.OutInformation import OutInformation


class Tags:

    @classmethod
    def clean_text(cls, elem: BeautifulSoup):
        if elem == OutInformation.RESOURCE_NOT_FOUND:
            return elem
        return cls.evaluate_clean_text(elem)

    @classmethod
    def evaluate_clean_text(cls, elem: BeautifulSoup):
        text = ''
        [remove_sup.extract() for remove_sup in elem.findAll('sup')]
        for e in elem.descendants:
            if isinstance(e, str):
                text += e
            elif e.name in ['br', 'p', 'li']:
                text += '\n'

        list_data = [x for x in text.strip().splitlines() if x != '']

        if not list_data:
            list_data = cls.__text_and_link(elem)

        return list_data[0] if len(list_data) == 1 else list_data

    @staticmethod
    def catch_error(section, data_source):
        div = section.find("div", {"data-source": data_source})
        return div.find("div", {"class": "pi-data-value pi-font"}) if div else OutInformation.RESOURCE_NOT_FOUND

    @staticmethod
    def custom_catch_error(soup: BeautifulSoup, tag: str, identification: str, name: str):
        div = soup.find(tag, {identification: name})
        return div if div else OutInformation.RESOURCE_NOT_FOUND

    @staticmethod
    def __text_and_link(soup: BeautifulSoup):
        tupla = soup.findAll('a')
        return [{"title": data.get('title'), "url": URL.URL_BASE[:-1] + data.get('href')} for data in tupla]
