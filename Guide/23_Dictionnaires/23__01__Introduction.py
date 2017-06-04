from random import choice, sample

cartes = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Cartes: {}".format(" ".join(cartes.keys())))
print("Points: {}".format(list(cartes.values())))

print("1\ Itération standard sur un dictionnaire")
for carte, valeur in cartes.items():
    print("la carte {} vaut {}".format(carte, valeur))

print("2\ Itération ordonnée sur un dictionnaire")
for carte in sorted(cartes.keys()):
    print("la carte {} vaut {}".format(carte, cartes[carte]))

print("3\ Black Jack")
liste_cartes = list(cartes)

print("Vous avez choisi:", end=" ")
carte = choice(liste_cartes)
score = cartes[carte]
print(carte, end=" ")
carte = choice(liste_cartes)
score += cartes[carte]
print(carte, end=" ")
print(" >>> votre score est de", score)

main_banque = sample(liste_cartes, 2)
score_banque = sum(cartes[carte] for carte in main_banque)
print("La banque a: {} {}  >> son score est de {}".format(main_banque[0],
                                                          main_banque[1],
                                                          score_banque))

