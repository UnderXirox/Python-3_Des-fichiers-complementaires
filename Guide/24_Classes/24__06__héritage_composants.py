class AffichableMixin:

    str_format = "PrettyPrintableObject"

    def __str__(self):
        """
        Représentation automatique d'un objet,
        basée sur l'utlisation une chaîne de formattage
        qui est un attribut de la classe
        """
        return self.str_format.format(self=self)

class NomAutomatiqueMixin:

    ordinal = 65

    def __init__(self):
        self.lettre = chr(NomAutomatiqueMixin.ordinal)
        NomAutomatiqueMixin.ordinal += 1

class Point(AffichableMixin, NomAutomatiqueMixin):
    """Représente un point dans l'espace"""

    str_format = "Point {self.lettre} ({self.x}, {self.y}, {self.z})"

    def __init__(self, x, y, z):
        """Méthode d'initialisation d'un point dans l'espace"""
        super().__init__()
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

    def __iadd__(self, other):
        """Opérateur d'addition en place"""
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        """Opérateur de soustraction en place"""
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, scalaire):
        """Opérateur de multiplication en place"""
        self.x *= scalaire
        self.y *= scalaire
        self.z *= scalaire
        return self


class Point2D(Point):
    """Représente un point dans le plan"""

    str_format = "Point2D {self.lettre} ({self.x}, {self.y})"

    def __init__(self, x, y):
        """Méthode d'initialisation d'un point dans le plan"""
        super().__init__(x, y, 0)


p = Point(1, 2, 3)
print(p)
p = Point2D(1, 2)
print(p)

