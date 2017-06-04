"""
Introduction aux Blocs conditionnels.

Un bloc conditionnel peut tester différentes conditions
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
if nombre1 <= nombre2:
    print(nombre1, "<=", nombre2)
elif nombre1 >= nombre2:
    print(nombre1, ">=", nombre2)
else:
    print(nombre1, "==", nombre2)

