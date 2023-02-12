import requests as requests
from bs4 import BeautifulSoup

from DragonBall.Constants.ScrapSagas import ScrapSagas
from DragonBall.Constants.URLS import URL
from DragonBall.Data.OutInformation import OutInformation
from DragonBall.Soup.section import Section
from DragonBall.Soup.summary import Summary
from DragonBall.Soup.tags import Tags


class Sagas:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def saga_list(cls, saga_list: list):
        return [Sagas(i).saga_information() for i in saga_list]

    @staticmethod
    def list():
        request = requests.get(URL.URL_LIST_CHRONO)
        soup = BeautifulSoup(request.content.decode('utf-8'), "html.parser")
        summary_data = soup.find("div", {"id": "toc"}).text.strip().splitlines()
        return Summary.clean_list_summary(summary_data, [1, -2])

    def saga_information(self):
        url = URL.URL_WIKI + self.name.replace(" ", "_")
        request = requests.get(url)
        soup = BeautifulSoup(request.content.decode('utf-8'), "html.parser")
        list_section = Section.obtain_section_data(soup, 'aside')
        basic_dict = self.__obtain_basic_data(soup, url)
        section_dict = self.__evaluate_scrapper_section(list_section, list(list_section.keys()), ScrapSagas)
        return self.__show_information(basic_dict, section_dict)

    def __obtain_basic_data(self, soup: BeautifulSoup, url: str):
        name = self.__get_official_name(soup, "h1", "id", "firstHeading")
        image = self.__get_image(soup, "a", "class", "image image-thumbnail")
        description = self.__get_description_saga(soup)
        return {"url": url, "name": name, "image": image, "descripcion": description}

    @staticmethod
    def __get_official_name(soup: BeautifulSoup, tag: str, identification: str, element: str):
        official_name = Tags.custom_catch_error(soup, tag, identification, element)
        return official_name.get_text(strip=True) if official_name else OutInformation.RESOURCE_NOT_FOUND

    @staticmethod
    def __get_image(soup: BeautifulSoup, tag: str, identification: str, name: str):
        if soup.find(tag, attrs={identification: name}):
            return soup.find(tag, attrs={identification: name}).get("href")
        return OutInformation.RESOURCE_NOT_FOUND


    @staticmethod
    def __get_description_saga(soup: BeautifulSoup):
        [remove_sup.extract() for remove_sup in soup.findAll('sup')]
        try:
            return next(p.text.strip() for header in soup.find_all(['h2', 'h3']) if (p := header.find_next_sibling('p')))
        except StopIteration:
            return OutInformation.RESOURCE_NOT_FOUND

    def __evaluate_scrapper_section(self, list_dict, list_search, tag_found: ScrapSagas):
        self.__return_empty_section(list_dict)
        names = list_dict.get(list(tag_found.sections.values())[0], OutInformation.RESOURCE_NOT_FOUND)
        data = list_dict.get(list(tag_found.sections.values())[1], OutInformation.RESOURCE_NOT_FOUND)
        serialization = list_dict.get(list(tag_found.sections.values())[2], OutInformation.RESOURCE_NOT_FOUND)

        return {
            "nombres": self.__names_section(names, tag_found.names) if list(tag_found.sections.values())[
                                                                           0] in list_search else names,
            "data": self.__data_section(data, tag_found.data) if list(tag_found.sections.values())[
                                                                     1] in list_search else data,
            "serializacion": self.__serialization_section(serialization, tag_found.serialization) if list(tag_found.sections.values())[
                                                                         2] in list_search else serialization,
        }

    @staticmethod
    def __return_empty_section(list_dict: dict):
        if not list_dict:
            return {"nombres": OutInformation.RESOURCE_NOT_FOUND, "data": OutInformation.RESOURCE_NOT_FOUND,
                    "serializacion": OutInformation.RESOURCE_NOT_FOUND}

    @staticmethod
    def __names_section(name, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(name, value)) for key, value in lista_tags.items()}

    @staticmethod
    def __data_section(data, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(data, value)) for key, value in lista_tags.items()}

    @staticmethod
    def __serialization_section(debut, lista_tags):
        return {key: Tags.clean_text(Tags.catch_error(debut, value)) for key, value in lista_tags.items()}

    @staticmethod
    def __show_information(dictionary_basic, dictionary_sections):
        dictionary = {
            "name": dictionary_basic['name'],
            "image": dictionary_basic['image'],
            "description": dictionary_basic['descripcion'],
            "names": dictionary_sections['nombres'],
            "data": dictionary_sections['data'],
            "serialization": dictionary_sections['serializacion'],
            "url_scrap": dictionary_basic['url']
        }
        return OutInformation.clean_not_found_scrape(dictionary)
