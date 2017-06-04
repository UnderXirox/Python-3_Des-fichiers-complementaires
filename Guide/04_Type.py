"""
Conversion vers un entier et comparaison

(tester avec une saisie qui n'est pas un nombre)
"""

# Premier nombre
nombre1 = input("Saisissez un premier nombre: ")
nombre1 = int(nombre1)

# Second nombre
nombre2 = int(input("Saisissez un second nombre: "))

# Faire la comparaison
comparaison = nombre1 < nombre2

print(nombre1, "<", nombre2, ":", comparaison)

