class Szescian:

    def __init__(self, bokSzescianu):
        self.bok = bokSzescianu
        self.pole = (self.bok ** 2) * 6
        self.objetosc = self.bok ** 3


class Prostopadloscian:

    def __init__(self, bokProstopadloscianu1, bokProstopadloscianu2, bokProstopadloscianu3):
        self.bok1 = bokProstopadloscianu1
        self.bok2 = bokProstopadloscianu2
        self.bok3 = bokProstopadloscianu3
        self.pole = self.bok1 * self.bok2 * 2 + self.bok1 * self.bok3 * 2 + self.bok2 * self.bok3 * 2
        self.objetosc = self.bok1 * self.bok2 * self.bok3


class Kula:

    def __init__(self, promien):
        self.promien = promien
        self.pole = 4 * 3.14 * self.promien ** 2
        self.objetosc = (4/3) * 3.14 * self.promien ** 3