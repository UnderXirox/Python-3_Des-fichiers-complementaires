class Point:
    """Représente un point dans l'espace"""

    def __init__(self, x, y, z):
        """Méthode d'initialisation d'un point dans l'espace"""
        self.x = x
        self.y = y
        self.z = z

    def afficher(self):
        """Méthode temporaire utilisée pour afficher notre point"""
        print("Point ({}, {}, {})".format(self.x, self.y, self.z))

    def module(self):
        """Renvoi le module du point"""
        return (self.x**2 + self.y**2 + self.z**2) ** (1 / 2)

    def distance(self, other):
        """
        Renvoi la distance par rapport à un autre point
        Les variables self et other sont toutes les deux des points.
        """
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

    def distance_et_module(self, other=None):
        """Renvoi la distance par rapport à un autre point ou par défaut à l'origine"""
        if other is None:
            other = Point(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)


p = Point(1, 2, 3)
p.afficher()
print("|p| =", p.module())
print("distance entre p et (1, 2, 5) est ", p.distance(Point(1, 2, 5)))
print("|p| =", p.distance_et_module())
print("distance entre p et (1, 2, 5) est ", p.distance_et_module(Point(1, 2, 5)))

