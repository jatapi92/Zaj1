class Telefon:

    def __init__(self, model, producent):
        self.model = model
        self.producent = producent


class Komunikacja:

    def wyslij_wiadomosc(self, odbiorca, utwor):
        pass


class Rozrywka:

    def odtworz_muzyke(self, utwor):
        pass

class Smartphon(Telefon):

    def __init__(self, model, producent, Komunikacja, Rozrywka):
        super().__init__(model, producent)
        self.Komunikacja = Komunikacja
        self.Rozrywka = Rozrywka
