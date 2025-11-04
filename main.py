from mapbook_lib.controller import user_info, add_user, remove_user, update_user, get_map
from mapbook_lib.model import users

def main():
    while True:
        print('==================MENU==================')
        print('0. Wyjście z programu')
        print('1. Wyświetlanie znajomych')
        print('2. Dodawanie znajomego')
        print('3. Usuwanie znajomego')
        print('4. Aktualizacji znajomego')
        print('5. Generuj mapę')
        print('========================================')
        tmp_choice: int = int(input('Wybierz opcje menu: '))
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


if __name__ == '__main__':
    main()