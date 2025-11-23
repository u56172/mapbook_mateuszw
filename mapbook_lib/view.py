from tkinter import *
import tkintermapview
from mapbook_lib.controller import add_user, user_info, delete_user, user_details, edit_user, update_user
from mapbook_lib.model import users


class MapBookView:
    def __init__(self):
        self.root = Tk()
        self.root.title('mapbook')
        self.root.geometry('1025x760')

        # Frames
        self.ramka_lista_obiektow = Frame(self.root)
        self.ramka_formularz = Frame(self.root)
        self.ramka_szczegoly_obiektu = Frame(self.root)
        self.ramka_mapa = Frame(self.root)

        self.ramka_lista_obiektow.grid(row=0, column=0)
        self.ramka_formularz.grid(row=0, column=1)
        self.ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
        self.ramka_mapa.grid(row=2, column=0, columnspan=2)

        # LISTA OBIEKTÓW
        self.label_lista_obiektow = Label(self.ramka_lista_obiektow, text='LISTA OBIEKTÓW')
        self.label_lista_obiektow.grid(row=0, column=0, columnspan=3)

        self.listbox_lista_obiektow = Listbox(self.ramka_lista_obiektow)
        self.listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

        self.button_pokaz_szczegoly = Button(
            self.ramka_lista_obiektow,
            text='Pokaż szczegóły',
            command=lambda: user_details(self, users)
        )
        self.button_pokaz_szczegoly.grid(row=2, column=0)

        self.button_usun_obiekt = Button(
            self.ramka_lista_obiektow,
            text='Usuń obiekt',
            command=lambda: delete_user(self, users)
        )
        self.button_usun_obiekt.grid(row=2, column=1)

        self.button_edytuj_obiekt = Button(
            self.ramka_lista_obiektow,
            text='Edytuj obiekt',
            command=lambda: edit_user(self, users)
        )
        self.button_edytuj_obiekt.grid(row=2, column=2)

        # FORMULARZ
        self.label_formularz = Label(self.ramka_formularz, text='Formularz: ')
        self.label_formularz.grid(row=0, column=0, columnspan=2)

        self.label_imie = Label(self.ramka_formularz, text='Imie: ')
        self.label_imie.grid(row=1, column=0, sticky=W)

        self.label_lokalizacja = Label(self.ramka_formularz, text='Lokalizacja: ')
        self.label_lokalizacja.grid(row=2, column=0, sticky=W)

        self.label_posty = Label(self.ramka_formularz, text='Posty: ')
        self.label_posty.grid(row=3, column=0, sticky=W)

        self.label_photo = Label(self.ramka_formularz, text='Obrazek: ')
        self.label_photo.grid(row=4, column=0, sticky=W)

        self.entry_name = Entry(self.ramka_formularz)
        self.entry_name.grid(row=1, column=1)

        self.entry_lokalizacja = Entry(self.ramka_formularz)
        self.entry_lokalizacja.grid(row=2, column=1)

        self.entry_posty = Entry(self.ramka_formularz)
        self.entry_posty.grid(row=3, column=1)

        self.entry_photo = Entry(self.ramka_formularz)
        self.entry_photo.grid(row=4, column=1)

        self.button_dodaj_obiekt = Button(
            self.ramka_formularz,
            text='Dodaj obiekt',
            command=lambda: add_user(self, users)
        )
        self.button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

        # SZCZEGÓŁY
        self.label_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Szczegoly obiektu')
        self.label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

        self.label_imie_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Imie: ')
        self.label_imie_szczegoly_obiektu.grid(row=1, column=0)

        self.label_imie_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

        self.label_lokalizacja_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Lokalizacja: ')
        self.label_lokalizacja_szczegoly_obiektu.grid(row=1, column=2)

        self.label_lokalizacja_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=3)

        self.label_posty_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Posty: ')
        self.label_posty_szczegoly_obiektu.grid(row=1, column=4)

        self.label_posty_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)

        # MAPA
        self.map_widget = tkintermapview.TkinterMapView(
            self.ramka_mapa,
            width=1025,
            height=600,
            corner_radius=0
        )
        self.map_widget.grid(row=0, column=0, columnspan=3)
        self.map_widget.set_position(deg_x=52.2, deg_y=21.0)
        self.map_widget.set_zoom(6)

    def run(self):
        self.root.mainloop()
