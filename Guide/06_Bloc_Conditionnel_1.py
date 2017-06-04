"""
Introduction aux Blocs conditionnels.

Un bloc est, une portion de code indentée différemment

Un bloc conditionnel s'exécute si une condition est vraie
"""
import sys

try:
    nombre1 = int(input("Saisissez un premier nombre: "))
    nombre2 = int(input("Saisissez un second nombre: "))
except ValueError as e:
    print("La conversion d'au moins un des nombres s'est mal passée",
          file=sys.stderr)
    sys.exit()

# Faire la comparaison
if nombre1 == nombre2:
    print(nombre1, "==", nombre2)
else:
    print(nombre1, "!=", nombre2)

