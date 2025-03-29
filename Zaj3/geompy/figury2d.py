class Kwadrat:

    def __init__(self, bokKwadratu):
        self.bok = bokKwadratu
        self.pole = self.bok ** 2
        self.obwod = 4 * self.bok


class Prostokat:

    def __init__(self, bokProstokata1, bokProstokata2):
        self.bok1 = bokProstokata1
        self.bok2 = bokProstokata2
        self.pole = self.bok1 * self.bok2
        self.obwod = 2 * self.bok1 + 2 * self.bok2


class Kolo:

    def __init__(self, promien):
        self.promien = promien
        self.pole = 3.14 * (promien ** 2)
        self.obwod = 2 * 3.14 * promien