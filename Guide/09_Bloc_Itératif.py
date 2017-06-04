"""
Introduction aux Blocs itératifs.

Un bloc itératifs permet de recommencer une action 0 à n fois.
"""

nombre = input("Saisissez un nombre entre 1 et 10: ")

try:
    nombre = int(nombre)
except:
    nombre = 0

while not 1 <= nombre <= 10:
    # Le nombre n'est pas valide

    # On redemande la saisie d'un nombre
    nombre = input("Saisissez un nombre entre 1 et 10: ")

    try:
        nombre = int(nombre)
    except:
        nombre = 0

print("On est certain que", nombre, "est un nombre et est compris entre 1 et 10 inclus.")

