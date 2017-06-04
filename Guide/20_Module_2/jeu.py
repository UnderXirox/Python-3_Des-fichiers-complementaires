"""
Module regroupant les fonctions décrivant la logique interne du jeu
"""

from saisie import (
    demander_saisie_nombre,
    demander_saisie_nombre_borne,
    demander_saisie_oui_ou_non,
)


def jouer_un_coup(nombre, minimum, maximum):
    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
        minimum = essai + 1
        victoire = False
    elif essai > nombre:
        print("Trop grand")
        maximum = essai - 1
        victoire = False
    else:
        print("Gagné!")
        victoire = True
        minimum = maximum = essai
    return victoire, minimum, maximum


def demander_saisie_du_nombre_mystere(minimum, maximum):
    return demander_saisie_nombre_borne("Saisissez le nombre à deviner",
                                        minimum, maximum)


def jouer_une_partie(nombre, minimum, maximum):
    while True:
        # On entre dans une boucle infinie
        # qui permet de jouer plusieurs coups

        victoire, minimum, maximum = jouer_un_coup(nombre, minimum, maximum)

        if (victoire):
            return


def decider_bornes():
    while True:
        minimum = demander_saisie_nombre("Quelle est la borne minimale ?")
        maximum = demander_saisie_nombre("Quelle est la borne maximale ?")
        if maximum > minimum:
            return minimum, maximum


def jouer():
    minimum, maximum = decider_bornes()
    while True:
        nombre = demander_saisie_du_nombre_mystere(minimum, maximum)
        jouer_une_partie(nombre, minimum, maximum)
        if not demander_saisie_oui_ou_non("Souhaitez-vous refaire une nouvelle partie ?"):
            print("A bientôt !")
            return

