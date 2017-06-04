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


p = Point(1, 2, 3)
p.afficher()

