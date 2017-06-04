"""
Introduction aux Blocs itératifs.

La boucle infinie doit être quittée à un moment ou à un autre.
Dans cet exemple, la boucle est forcément exécutée au moins une fois.
"""


while True:
    # On entre dans une boucle infinie

    # On demande la saisie d'un nombre
    nombre = input("Saisissez un nombre entre 1 et 10: ")

    try:
        nombre = int(nombre)
    except:
        pass
    else:
        # Faire la comparaison
        if 1 <= nombre <= 10:
            # On a ce que l'on veut, on quitte la boucle
            break

print("On est certain que", nombre, "est un nombre et est compris entre 1 et 10 inclus")

