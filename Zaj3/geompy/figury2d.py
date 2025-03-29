class Kwadrat:

    def __init__(self, bok_kwadratu):
        self.bok = bok_kwadratu
        self.pole = self.bok ** 2
        self.obwod = 4 * self.bok


class Prostokat:

    def __init__(self, bok_prostokata1, bok_prostokata2):
        self.bok1 = bok_prostokata1
        self.bok2 = bok_prostokata2
        self.pole = self.bok1 * self.bok2
        self.obwod = 2 * self.bok1 + 2 * self.bok2


class Kolo:

    def __init__(self, promien):
        self.promien = promien
        self.pole = 3.14 * (promien ** 2)
        self.obwod = 2 * 3.14 * promien