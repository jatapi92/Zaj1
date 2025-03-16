import json

class ModelAI:

    liczba_modeli = 0


    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.nowy_model()

    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, filename):
        with open(filename, 'r') as f:
            text = json.load(f)
        return text['name'], text['version']