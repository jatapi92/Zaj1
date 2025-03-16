
class Matrix:


    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return (f"[{self.a}, {self.b};\n{self.c}, {self.d}]")

    def __repr__(self):
        return (f"({self.a},{self.b},{self.c},{self.d})")


    def __add__(self, other):
        return Matrix(
            a = self.a + other.a,
            b = self.b + other.b,
            c = self.c + other.c,
            d = self.d + other.d
        )

    def __mul__(self, other):
        return Matrix(
            a = self.a * other.a + self.b * other.c,
            b = self.a * other.b + self.b * other.d,
            c = self.c * other.a + self.d * other.c,
            d = self.c * other.b + self.d * other.d
        )
