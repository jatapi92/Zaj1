class Szescian:

    def __init__(self, bok_szescianu):
        self.bok = bok_szescianu
        self.pole = (self.bok ** 2) * 6
        self.objetosc = self.bok ** 3


class Prostopadloscian:

    def __init__(self, bok_prostopadloscianu1, bok_prostopadloscianu2, bok_prostopadloscianu3):
        self.bok1 = bok_prostopadloscianu1
        self.bok2 = bok_prostopadloscianu2
        self.bok3 = bok_prostopadloscianu3
        self.pole = self.bok1 * self.bok2 * 2 + self.bok1 * self.bok3 * 2 + self.bok2 * self.bok3 * 2
        self.objetosc = self.bok1 * self.bok2 * self.bok3


class Kula:

    def __init__(self, promien):
        self.promien = promien
        self.pole = 4 * 3.14 * self.promien ** 2
        self.objetosc = (4/3) * 3.14 * self.promien ** 3