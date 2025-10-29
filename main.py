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

def add_user(users_data: list) -> None:
    print('Wybrano funkcje dodawania znajomego')
    name: str = input('Enter your name: ')
    location: str = input('Enter your location: ')
    posts: int = int(input('Enter number of posts: '))
    users_data.append({'name': name, 'location': location, 'posts': posts})
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

if __name__ == '__main__':
    while True:
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
