"""
Module regroupant toutes les fonctionnalités
permettant de demander une saisie de nombres
"""


import sys


MIN=0
MAX=100


def demander_saisie_nombre(invite):
    """
    Cette fonction se contente de vérifier que l'on a bien à faire à un nombre
    """
    while True:
        # On entre dans une boucle infinie

        # On demande la saisie d'un nombre
        print(invite, end=": ")
        saisie = input()

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
    """
    while True:
        # On entre dans une boucle infinie

        # On demande la saisie d'un nombre
        invite = "{} entre {} et {} inclus".format(invite, minimum, maximum)
        saisie = demander_saisie_nombre(invite)

        if minimum <= saisie <= maximum:
            # On a ce que l'on veut, on quitte la boucle en quittant la fonction
            return saisie

