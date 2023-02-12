from bs4 import BeautifulSoup


class Section:

    @classmethod
    def obtain_section_data(cls, soup: BeautifulSoup, tag: str):
        data_General = soup.find(tag)
        if data_General:
            sections = [i for i in data_General.find_all("section", {'class': 'pi-item pi-group pi-border-color'})]
            return cls.__find_name_section(sections)
        else:
            return dict()

    @staticmethod
    def __find_name_section(sections: BeautifulSoup):
        return {i.find('h2').text: i for i in sections if i.find('h2')}