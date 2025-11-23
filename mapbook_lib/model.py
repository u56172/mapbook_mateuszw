import requests
from bs4 import BeautifulSoup

users: list = []
class User:
    def __init__(self, name:str, location: str, posts: int, photo:str, map_widget):
        self.name = name
        self.location = location
        self.posts = posts
        self.photo = photo
        self.coords = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coords[0], self.coords[1], text=self.name)

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/118.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, 'html.parser')

        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return [latitude, longitude]

