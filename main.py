from tkinter import *
import os
import tkinter
import tkintermapview

from mapbook_lib.controller import update_user

#Logika biznesowa

users: list = []

import requests
from bs4 import BeautifulSoup

class User:
    def __init__(self, name:str, location: str, posts: int, photo:str):
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

def add_user(users_data: list) -> None:
    name: str = entry_name.get()
    location: str = entry_lokalizacja.get()
    post: int=int(entry_posty.get())
    photo: str = entry_photo.get()
    users_data.append(User(name=name, location=location, posts=post, photo=photo))
    print(users_data)
    user_info(users_data)

    entry_name.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_posty.delete(0, END)
    entry_photo.delete(0, END)
    entry_name.focus()

def user_info(users_data: list) -> None:
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users_data):
        listbox_lista_obiektow.insert(idx,f'{user.name} {user.location} {user.posts}')

def delete_user(users_data: list) -> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    users.data[i].marker.delete()
    users_data.pop(i)
    user_info(users_data)

def user_details(users_data: list) -> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=users_data[i].name)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users_data[i].location)
    label_posty_szczegoly_obiektu_wartosc.config(text=users_data[i].posts)
    map_widget.set_position(users_data[i].coords[0],users_data[i].coords[1])
    map_widget.set_zoom(16)

def edit_user(users_data: list) -> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_name.insert(0, users_data[i].name)
    entry_lokalizacja.insert(0, users_data[i].location)
    entry_posty.insert(0, users_data[i].posts)
    entry_photo.insert(0, users_data[i].photo)

    button_dodaj_obiekt.config(text='Zapisz zmiany', command=lambda: update_user(users_data, i))

def update_user(users_data: list, i) -> None:
    users_data[i].name = entry_name.get()
    users_data[i].location = entry_lokalizacja.get()
    users_data[i].posts = int(entry_posty.get())
    users_data[i].photo = entry_photo.get()

    users_data[i].coords = users_data[i].get_coordinates()
    users_data[i].marker.set_position(users_data[i].coords[0], users_data[i].coords[1])
    users_data[i].marker.set_text(text=users_data[i].name)

    user_info(users_data)

    button_dodaj_obiekt.config(text='Dodaj użytkownika', command=lambda: add_user(users_data))
    entry_name.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_posty.delete(0, END)
    entry_photo.delete(0, END)
    entry_name.focus()




root = Tk()
root.title('mapbook')
root.geometry('1025x760')


ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# RAMKA LISTA OBIEKTÓW
label_lista_obiektow = Label(ramka_lista_obiektow, text='LISTA OBIEKTÓW')
label_lista_obiektow.grid(row=0, column=0, columnspan=3)

listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaż szczegóły', command= lambda: user_details(users_data=users))
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń obiekt', command= lambda: delete_user(users_data=users))
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command= lambda: edit_user(users_data=users))
button_edytuj_obiekt.grid(row=2, column=2)




# RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text='Formularz: ')
label_formularz.grid(row=0, column=0, columnspan=2)

label_imie = Label(ramka_formularz, text='Imie: ')
label_imie.grid(row=1, column=0, sticky=W)

label_lokalizacja = Label(ramka_formularz, text='Lokalizacja: ')
label_lokalizacja.grid(row=2, column=0, sticky=W)

label_posty = Label(ramka_formularz, text='Posty: ')
label_posty.grid(row=3, column=0, sticky=W)

label_photo = Label(ramka_formularz, text='Obrazek: ')
label_photo.grid(row=4, column=0, sticky=W)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)

entry_lokalizacja = Entry(ramka_formularz)
entry_lokalizacja.grid(row=2, column=1)

entry_posty = Entry(ramka_formularz)
entry_posty.grid(row=3, column=1)

entry_photo = Entry(ramka_formularz)
entry_photo.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj obiekt', command=lambda: add_user(users_data=users))
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)





# RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegoly obiektu')
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imie: ')
label_imie_szczegoly_obiektu.grid(row=1, column=0)

label_imie_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_lokalizacja_szczegoly_obiektu=Label(ramka_szczegoly_obiektu, text='Lokalizacja: ')
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=2)

label_lokalizacja_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=3)

label_posty_szczegoly_obiektu=Label(ramka_szczegoly_obiektu, text='Posty: ')
label_posty_szczegoly_obiektu.grid(row=1, column=4)

label_posty_szczegoly_obiektu_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)


# RAMKA MAPY

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1025, height=600, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=3)
map_widget.set_position(deg_x=52.2, deg_y=21.0)
map_widget.set_zoom(6)
root.mainloop()