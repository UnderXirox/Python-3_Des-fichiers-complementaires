from itertools import chain, product, repeat, cycle

liste = list("abc")

print("1\ Parcours classique d'une liste")
for lettre in liste:
    print(lettre)

print("2\ Si l'on a besoin d'un indice")
for indice, lettre in enumerate(liste):
    print("indice {}, lettre {}".format(indice, lettre))

print("3\ A ne pas faire")
tableau = [liste, liste]

tableau[0][0] = "X"
print("tableau = {}".format(tableau), "liste = {}".format(liste), sep="\n")

print("4\ Parcours d'un tableau")
liste = list("abc")

tableau = [liste[:], [c.upper() for c in liste]]

for ligne in tableau:
    for case in ligne:
        print(case)

print("5\ Parcours à plat d'un tableau")
for case in chain.from_iterable(tableau):
    print(case)

print("6\ Si l'on a besoin d'un indice")
for i, ligne in enumerate(tableau):
    for j, case in enumerate(ligne):
        print("tableau[{}][{}] = {}".format(i, j, case))

print("7\ Parcours par colonne puis par ligne")
transpose = zip(*tableau)

for j, colonne in enumerate(transpose):
    for i, case in enumerate(colonne):
        print("tableau[{}][{}] = {}".format(i, j, case))

print("8\ Tableaux crées virtuellement par le croisement de deux listes")
lignes = tableau[1][:]
colonnes = [1, 2, 3]

for ligne, colonne in product(lignes, colonnes):
    print("Case {}{}".format(ligne, colonne))

print("9\ Croiser une liste avec une donnée unique par le produit")
for ligne, colonne in product("Z", colonnes):
    print("Case {}{}".format(ligne, colonne))

print("10\ Croiser une liste avec une donnée unique par une répétition")
for ligne, colonne in zip(repeat("Z"), colonnes):
    print("Case {}{}".format(ligne, colonne))

print("11\ Croiser une liste avec une autre cyclique")
for numero, lettre in zip(range(10), cycle("ABC")):
    print("Case {}{}".format(lettre, numero))

