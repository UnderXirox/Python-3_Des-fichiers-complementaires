"""
Exercice: réaliser un jeu "Guess The number"

PARTIE 1: Demander la saisie à l'utilisateur d'un nombre entre 0 et 100
PARTIE 2: Faire deviner le nombre à l'utilisateur

Utiliser une fonction pour capitaliser le code commun
"""

def demander_saisie_nombre():
    while True:
        # On entre dans une boucle infinie
        # qui permet de corriger une erreur de saisie

        # On demande la saisie d'un nombre
        saisie = input("Saisissez un nombre entre 0 et 99 inclus: ")

        try:
            saisie = int(saisie)
        except:
            pass
        else:
            # Faire la comparaison
            if 9 <= saisie <= 99:
                # On a ce que l'on veut, on quitte la boucle
                break
    return saisie


# PARTIE 1
print("Saisissez le nombre à deviner")
nombre = demander_saisie_nombre()


# PARTIE 2
print("essayez de trouver le nombre à deviner")
while True:
    # On entre dans une boucle infinie
    # qui permet de jouer plusieurs coups

    essai = demander_saisie_nombre()

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
    elif essai > nombre:
        print("Trop grand")
    else:
        print "Gagné!"
        break

