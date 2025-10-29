zmienna_1: str = 'Kasia'
zmienna_2: str = 'Michasia'
zmienna_3: str = 'Zdzisia'
zmienna_4: str = 'Mateusz'

users: list = [
    {'name': zmienna_1, 'location': 'Washington', 'posts': 67},
    {'name': zmienna_2, 'location': 'Paris', 'posts': 22},
    {'name': zmienna_3, 'location': 'Michigan', 'posts': 55},
    {'name': zmienna_4, 'location': 'Warsaw', 'posts': 3}
]

def user_info(users_data: list) -> None:
    print('Wybrano funkcje wyświetlania aktywności znajomych')
    for user in users_data:
        print(f'Your user {user['name']}, from {user['location']}, has {user['posts']} posts.')

if __name__ == '__main__':
    while True:
        tmp_choice:int= int(input('Wybierz opcje menu: '))
        if tmp_choice == 0:
            break
        if tmp_choice == 1:
            user_info(users)
        if tmp_choice == 2:
            print('Wybrano funkcje dodawania znajomego')
        if tmp_choice == 3:
            print('Wybrano funkcje usuwania znajomych')
        if tmp_choice == 4:
            print('Wybrano funkcje aktualizacji znajomych')
