"""
Exercice: réaliser un jeu "Guess The number"

PARTIE 1: Demander la saisie à l'utilisateur d'un nombre entre 0 et 100
PARTIE 2: Faire deviner le nombre à l'utilisateur

"""

# PARTIE 1

# Pour l'exercice du premier chapitre, il faut utiliser ce qui suit :
# import random
# nombre = random.randint(0, 100)

# Pour la mise en évidence du second chapitre, il faut utiliser ce qui suit :
print("Saisissez le nombre à deviner")
while True:
    # On entre dans une boucle infinie

    # On demande la saisie d'un nombre
    nombre = input("Saisissez un nombre entre 0 et 99 inclus: ")

    try:
        nombre = int(nombre)
    except:
        pass
    else:
        # Faire la comparaison
        if 0 <= nombre <= 99:
            # On a ce que l'on veut, on quitte la boucle
            break

# PARTIE 2
print("essayez de trouver le nombre à deviner")
while True:  # BOUCLE 1
    # On entre dans une boucle infinie
    # qui permet de jouer plusieurs coups

    while True:  # BOUCLE 2
        # On entre dans une boucle infinie
        # qui permet de corriger une erreur de saisie

        # On demande la saisie d'un nombre
        essai = input("Saisissez un nombre entre 0 et 99 inclus: ")

        try:
            essai = int(essai)
        except:
            pass
        else:
            # Faire la comparaison
            if 0 <= essai <= 99:
                # On a ce que l'on veut, on quitte la BOUCLE 2
                break

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
    elif essai > nombre:
        print("Trop grand")
    else:
        print("Gagné!")
        # On a terminé la partie, on quitte la BOUCLE 1
        break

