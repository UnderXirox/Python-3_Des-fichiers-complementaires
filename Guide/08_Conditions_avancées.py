"""
Introduction aux Blocs conditionnels.

Un bloc conditionnel peut tester différentes conditions
"""
import sys


nombre1 = input("Saisissez un premier nombre entre 1 et 10: ")
nombre2 = input("Saisissez un second nombre entre 1 et 10: ")

try:
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
except:
    print("La conversion d'au moins un des nombres s'est mal passée",
          file=sys.stderr)
    sys.exit()

# Faire la comparaison
if 0 < nombre1 < 11:
    print("Le nombre", nombre1, "est bien entre 1 et 10")

if 1 <= nombre2 <= 10:
    print("Le nombre", nombre2, "est bien entre 1 et 10")

