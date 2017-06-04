class Point:
    """Représente un point dans l'espace"""

    def __init__(self, x, y, z):
        """Méthode d'initialisation d'un point dans l'espace"""
        self.x, self.y, self.z = x, y, z

    def distance(self, other=None):
        """Renvoi la distance par rapport à un autre point ou par défaut à l'origine"""
        if other is None:
            other = Point(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

    def __add__(self, other):
        """Opérateur d'addition"""
        return Point(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)

    def __sub__(self, other):
        """Opérateur de soustraction"""
        return Point(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)

    def __mul__(self, scalaire):
        """Opérateur de multiplication"""
        return Point(self.x * scalaire,
                     self.y * scalaire,
                     self.z * scalaire)

    def __str__(self):
        """Représentation d'un point sous la forme d'une chaîne de caractère"""
        return "Point ({self.x}, {self.y}, {self.z})".format(self=self)


p = Point(1, 2, 3)
print(p * 3)

print("Mise en évidence d'un problème d'optimisation")
print(id(p))
p *= 42
print(id(p))
print(p)

