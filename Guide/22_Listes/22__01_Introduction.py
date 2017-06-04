liste = list("Python is awesome")

# Affichage de la liste
print("liste = ", liste)
# accès à un membre de la liste (get)
print("liste[4] = ", liste[4])
print("liste[-3] = ", liste[-3])

# extraction de sous-liste
print("liste[:6] = ", liste[:6])
print("liste[7:9] = ", liste[7:9])
print("liste[10:] = ", liste[10:])
print("liste[2::5] = ", liste[2::5])
print("liste[-3::-6] = ", liste[-3::-6])

# écriture d'un membre de la liste (set)
liste[11] = "b"
print("""liste[11] = "b" """)
print("liste = ", liste)

print("""liste[13:15] = "fg" """)
liste[13:15] = "fg"
print("liste = ", liste)

# suppression d'un membre de la liste (del)
print("""del liste[15]""")
del liste[15]
print("liste = ", liste)

print("""liste.remove("y")""")
liste.remove("y")
print("liste = ", liste)

print("""while " " in liste: liste.remove(" ")""")
while " " in liste:
    liste.remove(" ")
print("liste = ", liste)

print("""del liste[:7]""")
del liste[:7]
print("liste = ", liste)

# Suppression du dernier élément (et renvoie de celui-ci)
print("""liste.pop() -> Renvoie :""", liste.pop())
print("liste = ", liste)

# Ajout d'un élément à la fin de la liste
print("""liste.append("h")""")
liste.append("h")
print("liste = ", liste)

# Ajout d'un élément n'importe ou dans la liste
print("""liste.insert(2, "d")""")
liste.insert(2, "d")
print("liste = ", liste)

print("""liste.insert(2, "c")""")
liste.insert(2, "c")
print("liste = ", liste)

# Concaténation d'une liste
print("""liste.extend(["i", "j"])""")
liste.extend(["i", "j"])
print("liste = ", liste)

#
# Exercice 1: Utilisez les fonctions précédentes pour ajouter les éléments manquants
# Exercice 2: Utiliser les fonctions précédentes pour supprimer des éléments en trop

def exercice1():
    liste = ["P", "t"]
    # TODO
    assert "".join(liste) == "Python"

def exercice2():
    liste = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    # TODO
    assert liste == list(range(1, 6))

