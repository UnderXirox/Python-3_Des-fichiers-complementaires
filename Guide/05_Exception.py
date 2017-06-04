"""
Introduction aux exceptions
"""
import sys

# Premier nombre
nombre1 = input("Saisissez un premier nombre: ")
try:
    nombre1 = int(nombre1)
except:
    print("La conversion d'au moins un des nombres s'est mal passée",
          file=sys.stderr)
    sys.exit()

# Second nombre
try:
    nombre2 = int(input("Saisissez un second nombre: "))
except ValueError as e:
    print("La conversion d'au moins un des nombres s'est mal passée",
          file=sys.stderr)
    sys.exit()

# Faire la comparaison
comparaison = nombre1 < nombre2

print(nombre1, "<", nombre2, ":", comparaison)

