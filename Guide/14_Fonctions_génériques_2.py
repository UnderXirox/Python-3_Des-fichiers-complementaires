"""
Exercice: réaliser un jeu "Guess The number"

PARTIE 1: Demander la saisie à l'utilisateur d'un nombre entre 0 et 100
PARTIE 2: Faire deviner le nombre à l'utilisateur

Utiliser une fonction pour capitaliser le code commun
"""

MIN = 0
MAX = 99


def demander_saisie_nombre(invite, minimum, maximum):
    # Compléter l'invite:
    invite += " entre " + str(minimum) + " et " + str(maximum) + " inclus: "

    while True:
        # On entre dans une boucle infinie

        # On demande la saisie d'un nombre
        saisie = input(invite)

        try:
            saisie = int(saisie)
        except:
            pass
        else:
            # Faire la comparaison
            if minimum <= saisie <= maximum:
                # On a ce que l'on veut, on quitte la boucle
                break
    return saisie


# PARTIE 1
nombre = demander_saisie_nombre("Saisissez le nombre à deviner", MIN, MAX)


# PARTIE 2
while True:
    # On entre dans une boucle infinie
    # qui permet de jouer plusieurs coups

    essai = demander_saisie_nombre("Devinez le nombre", MIN, MAX)

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
    elif essai > nombre:
        print("Trop grand")
    else:
        print("Gagné!")
        break

