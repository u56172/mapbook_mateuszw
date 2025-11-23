from mapbook_lib.model import User, users


def add_user(view, users_data: list) -> None:
    name: str = view.entry_name.get()
    location: str = view.entry_lokalizacja.get()
    post: int = int(view.entry_posty.get())
    photo: str = view.entry_photo.get()

    user = User(name=name, location=location, posts=post, photo=photo, map_widget=view.map_widget)
    users_data.append(user)

    user_info(view, users_data)

    view.entry_name.delete(0, 'end')
    view.entry_lokalizacja.delete(0, 'end')
    view.entry_posty.delete(0, 'end')
    view.entry_photo.delete(0, 'end')
    view.entry_name.focus()


def user_info(view, users_data: list) -> None:
    view.listbox_lista_obiektow.delete(0, 'end')
    for idx, user in enumerate(users_data):
        view.listbox_lista_obiektow.insert(idx, f'{user.name} {user.location} {user.posts}')


def delete_user(view, users_data: list) -> None:
    i = view.listbox_lista_obiektow.index('active')

    users_data[i].marker.delete()
    users_data.pop(i)

    user_info(view, users_data)


def user_details(view, users_data: list) -> None:
    i = view.listbox_lista_obiektow.index('active')

    view.label_imie_szczegoly_obiektu_wartosc.config(text=users_data[i].name)
    view.label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users_data[i].location)
    view.label_posty_szczegoly_obiektu_wartosc.config(text=users_data[i].posts)

    view.map_widget.set_position(users_data[i].coords[0], users_data[i].coords[1])
    view.map_widget.set_zoom(16)


def edit_user(view, users_data: list) -> None:
    i = view.listbox_lista_obiektow.index('active')

    view.entry_name.insert(0, users_data[i].name)
    view.entry_lokalizacja.insert(0, users_data[i].location)
    view.entry_posty.insert(0, users_data[i].posts)
    view.entry_photo.insert(0, users_data[i].photo)

    view.button_dodaj_obiekt.config(text='Zapisz zmiany', command=lambda: update_user(view, users_data, i))


def update_user(view, users_data: list, i) -> None:
    users_data[i].name = view.entry_name.get()
    users_data[i].location = view.entry_lokalizacja.get()
    users_data[i].posts = int(view.entry_posty.get())
    users_data[i].photo = view.entry_photo.get()

    users_data[i].coords = users_data[i].get_coordinates()
    users_data[i].marker.set_position(users_data[i].coords[0], users_data[i].coords[1])
    users_data[i].marker.set_text(users_data[i].name)

    user_info(view, users_data)

    view.button_dodaj_obiekt.config(text='Dodaj użytkownika', command=lambda: add_user(view, users_data))

    view.entry_name.delete(0, 'end')
    view.entry_lokalizacja.delete(0, 'end')
    view.entry_posty.delete(0, 'end')
    view.entry_photo.delete(0, 'end')
    view.entry_name.focus()
