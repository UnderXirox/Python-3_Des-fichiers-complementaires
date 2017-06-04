phrase = input("Saisissez une phrase: ")
# Exemple avec cEcI est l'abc du b_a_ba

print("Les mots sont les suivants:")
mots = phrase.split()
for mot in mots:
    print(mot)

# cEcI
# est
# l'abc
# du
# b_a_ba


separateur = input("Saisissez une chaîne de séparation: ")
# _

print("En utilisant ce séparateur, voici les mots trouvés:")
mots = phrase.split(separateur)
for mot in mots:
    print(mot)

# En utilisant ce séparateur, voici les mots trouvés:
# cEcI est l'abc du b
# a
# ba


glue = input("Choisissez avec quoi les recoller ensemble: ")
# *

print("Voici le mot recollé:")
print(glue.join(mots))

# Voici le mot recollé:
# cEcI est l'abc du b*a*ba

