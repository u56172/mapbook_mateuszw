zmienna_1:str = 'Kasia'
zmienna_2:str = 'Michasia'
zmienna_3:str = 'Zdzisia'
zmienna_4:str = 'Mateusz'

#przygotuj liste slownikow ktora bedzie przechowywac informacje o uzytkownikach na temat: imie(alias name)
#miejscowosc (location), liczba_postow(posts)
users:list = [
    {'name':zmienna_1, 'location': 'Washington', 'posts': 67},
    {'name':zmienna_2, 'location': 'Paris', 'posts': 22},
    {'name':zmienna_3, 'location': 'Michigan', 'posts': 55},
    {'name':zmienna_4, 'location': 'Warsaw', 'posts': 3}
    ]

for user in users:
    print(f'Your user {user['name']}, from {user['location']}, has {user['posts']} posts.')