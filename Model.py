import glob
import sqlite3
from datetime import datetime

from Score import Score


class Model:
    def __init__(self):
        self.__database = 'databases/hangman_words_ee.db'
        # pip install Pillow => vajalik piltidega majandamiseks
        self.__image_files = glob.glob('images/*.png')
        # TODO: juhuslik sõna,
        # TODO: kõik sisestatud tähed (List)
        # TODO: vigade lugeja (s.h. pildi id)
        # TODO: kasutaja leitud tähed (visuaal muidu on seal alakriips _)

    @property
    def database(self):
        return self.__database

    @property
    def image_files(self):
        return self.__image_files

    @property
    def word(self):
        return self.__word

    @property
    def correct_letters(self):
        return self.__correct_letters

    @property
    def wrong_letters(self):
        return self.__wrong_letters

    @property
    def wrong_count(self):
        return self.__wrong_count

    @database.setter
    def database(self, value):
        self.__database = value

    def read_scores_data(self):
        connection = None
        try:
            connection = sqlite3.connect(self.__database)
            sql = 'SELECT * FROM scores ORDER BY seconds;'
            cursor = connection.execute(sql)
            data = cursor.fetchall()
            result = []
            for row in data:
                result.append(Score(row[1], row[2], row[3], row[4], row[5]))

            return result
        except sqlite3.Error as error:
            print(f'Viga andmebaasiga {self.__database} ühendamisel: {error}')
        finally:
            if connection:
                connection.close()

    def new_game(self):
        self.__wrong_count = 0
        self.__letters = []
        self.__correct_letters = []
        self.__wrong_letters = []
        self.__word = self.random_word()
        self.__correct_letters = list("_" * len(self.__word))

    def random_word(self):
        connection = None
        try:
            connection = sqlite3.connect(self.__database)
            sql = 'SELECT word FROM words ORDER BY RANDOM() LIMIT 1;'
            cursor = connection.execute(sql)
            word = cursor.fetchone()[0]
            cursor.close()
            return word
        except sqlite3.Error as error:
            print(f'Viga andmebaasiga {self.__database} ühendamisel: {error}')
        finally:
            if connection:
                connection.close()

    # TODO: Meetod mis seadistab uue mängu
    # TODO: Seadistab uue sõna äraarvamiseks
    # TODO: Seadistab mõningate muutujate algväärtused (vaata __init__ kolme viimast TODO. Neljas muutuja on eelmine rida)
    # TODO: Seadistab ühe muutuja nii, et iga tähe asemel paneb alakriipsu mida näidata aknas äraarvatavas sõnas (LIST)

    # TODO: Meetod mis seadistab juhusliku sõna muutujasse
    # TODO: Teeb andmebaasi ühenduse ja pärib sealt ühe juhusliku sõna ning kirjutab selle muutujasse

    # TODO: Kasutaja sisestuse kontroll (Vaata Controlleris btn_send_click esimest TODO)
    # TODO: Kui on midagi sisestatud võta sisestusest esimene märk (me saame sisestada pika teksti aga esimene täht on oluline!)
    # TODO: Kui täht on otsitavas sõnas, siis asenda tulemuses alakriips õige tähega.
    # TODO: kui tähte polnud, siis vigade arv kasvab +1 ning lisa vigane täht eraldi list

    # TODO: Meetod mis tagastab vigaste tähtede listi asemel tulemuse stringina. ['A', 'B', 'C'] => A, B, C

    # TODO: MEetid mis lisab mängija ja tema aja andmebaasi (Vaata Controlleris viimast TODO rida)
    # TODO: Võtab hetke/jooksva aja kujul AAAA-KK-PP TT:MM:SS (Y-m-d H:M:S)
    # TODO: Kui kasutaja sisestas nime, siis eemalda algusest ja lõpust tühikud
    # TODO: Tee andmebaasi ühendus ja lisa kirje tabeisse scores. Salvesta andmed tabelis ja sulge ühendus.
