"""
Exercice: réaliser un jeu "Guess The number"

PARTIE 1: Demander la saisie à l'utilisateur d'un nombre entre 0 et 100
PARTIE 2: Faire deviner le nombre à l'utilisateur

Utiliser une fonction pour capitaliser le code commun
"""

import sys

MIN = 0
MAX = 99

def demander_saisie_nombre(invite):
    """
    Cette fonction se contente de vérifier que l'on a bien à faire à un nombre
    """
    while True:
        # On entre dans une boucle infinie

        # On demande la saisie d'un nombre
        saisie = input(invite + ": ")

        try:
            saisie = int(saisie)
        except:
            print("Seul les caractères [0-9] sont autorisés.", file=sys.stderr)
        else:
            # On a ce que l'on veut, on quitte la boucle en quittant la fonction
            return saisie

def demander_saisie_nombre_borne(invite, minimum=MIN, maximum=MAX):
    """
    Cette fonction utilise la précédente et rajoute une post-condition
    sur les bornes du nombre à saisir
    """# On demande la saisie d'un nombre
    invite = "{} entre {} et {} inclus".format(invite, minimum, maximum)

    while True:
        # On entre dans une boucle infinie

        saisie = demander_saisie_nombre(invite)

        if minimum <= saisie <= maximum:
            # On a ce que l'on veut, on quitte la boucle en quittant la fonction
            return saisie

# PARTIE 1
minimum = maximum = 0
while True:
    minimum = demander_saisie_nombre("Quelle est la borne minimale ?")
    maximum = demander_saisie_nombre("Quelle est la borne maximale ?")
    if maximum > minimum:
        break

nombre = demander_saisie_nombre_borne("Saisissez le nombre à deviner", minimum, maximum)



# PARTIE 2
while True:
    # On entre dans une boucle infinie
    # qui permet de jouer plusieurs coups

    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
        minimum = essai + 1
    elif essai > nombre:
        print("Trop grand")
        maximum = essai - 1
    else:
        print("Gagné!")
        break


