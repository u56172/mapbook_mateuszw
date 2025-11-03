import requests
from bs4 import BeautifulSoup

users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 67, 'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzMLxdppfv-CUL4j0KwPM9ALHXtxmeyyujaOwBiByXycbCwyQL-sxTtEzvojcRQrKEJwtS58BsnmYdUtrKQ38MnpST59JkSd6d5gaMZcI1&s=10'},
    {'name': 'Michasia', 'location': 'Kraków', 'posts': 22, 'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzMLxdppfv-CUL4j0KwPM9ALHXtxmeyyujaOwBiByXycbCwyQL-sxTtEzvojcRQrKEJwtS58BsnmYdUtrKQ38MnpST59JkSd6d5gaMZcI1&s=10'},
    {'name': 'Zdzisia', 'location': 'Wrocław', 'posts': 55, 'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzMLxdppfv-CUL4j0KwPM9ALHXtxmeyyujaOwBiByXycbCwyQL-sxTtEzvojcRQrKEJwtS58BsnmYdUtrKQ38MnpST59JkSd6d5gaMZcI1&s=10'}
]

def user_info(users_data: list) -> None:
    print('Wybrano funkcje wyświetlania aktywności znajomych')
    for user in users_data:
        print(f'Your user {user['name']}, from {user['location']}, has {user['posts']} posts.')

def add_user(users_data: list) -> None:
    print('Wybrano funkcje dodawania znajomego')
    name: str = input('Enter your name: ')
    location: str = input('Enter your location: ')
    posts: int = int(input('Enter number of posts: '))
    photo: str = input('Enter photo url: ')
    users_data.append({'name': name, 'location': location, 'posts': posts, 'photo': photo})
    print('User added!')

def remove_user(users_data: list) -> None:
    print('Wybrano funkcje usuwania znajomego')
    tmp_name: str = input('Enter your name: ')
    for user in users:
        if user['name'] == tmp_name:
            users.pop(users.index(user))

def update_user(users_data: list) -> None:
    print('Wybrano funkcje aktualizacji użytkownika')
    tmp_name: str = input('Enter old name: ')
    for user in users:
        if user['name'] == tmp_name:
            user['name'] = input('Enter new name: ')
            user['location'] = input('Enter new location: ')
            user['posts'] = input('Enter new amount of posts: ')
            user['photo'] = input('Enter new photo url: ')

def get_coordinates(city_name: str) -> list:
    url: str = f'https://pl.wikipedia.org/wiki/{city_name}'
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

def get_map(users_data: list) -> None:
    import folium
    print('Wybrano funkcje wyświetlania mapy')
    m = folium.Map(location=[52.23, 21.0], zoom_start=6)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(user['location']),
            tooltip="Click me!",
            popup=f'<center><h3><b>{user["name"]} {user["location"]} {user["posts"]}</b></h3></center>, <img src = {user['photo']}/> ',
            icon=folium.Icon(color='purple', border_color = 'pink', icon="star"),
        ).add_to(m)
    m.save('notatnik.html')


while True:
    print('==================MENU==================')
    print('0. Wyjście z programu')
    print('1. Wyświetlanie znajomych')
    print('2. Dodawanie znajomego')
    print('3. Usuwanie znajomego')
    print('4. Aktualizacji znajomego')
    print('5. Generuj mapę')
    print('========================================')
    tmp_choice:int= int(input('Wybierz opcje menu: '))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        user_info(users)
    if tmp_choice == 2:
        add_user(users)
    if tmp_choice == 3:
        remove_user(users)
    if tmp_choice == 4:
        update_user(users)
    if tmp_choice == 5:
        get_map(users)

# TODO model view controller
# TODO data scraping
# TODO interacive map
# TODO command pattern, registry pattern with decorator