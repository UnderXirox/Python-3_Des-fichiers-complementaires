phrase = input("Saisissez une phrase (avec min, Maj, Nb, accents, et espaces): ")
# Exemple avec cEcI est l'abc du b_a_ba

print("Minuscules        : " + phrase.lower())
print("Majuscules        : %s" % phrase.upper())
print("Phrase en capitale: {}".format(phrase.capitalize()))
print("Mots en capitale  :", phrase.title())

# Minuscules        : ceci est l'abc du b_a_ba
# Majuscules        : CECI EST L'ABC DU B_A_BA
# Phrase en capitale: Ceci est l'abc du b_a_ba
# Mots en capitale  : Ceci Est L'Abc Du B_A_Ba

print("Longueur de la chaîne: {}".format(len(phrase)))
# Longueur de la chaîne: 24

print("Votre phrase contient-elle la lettre 'a' ?", "a" in phrase)
print("Votre phrase contient-elle la séquence 'abc' ?", "abc" in phrase)

# Votre phrase contient-elle la lettre 'a' ? True
# Votre phrase contient-elle la séquence 'abc' ? True


nb = phrase.count("a")
print("Combien d'occurences de 'a' se trouvent dans la phrase ?", nb)
if nb > 0:
    index = phrase.find("a")
    print("Ou se trouve la première occurence de 'a' ?", index)
    for i in range(1, nb):
        index = phrase.find("a", index + 1)
        print("L'occurence numéro {} de 'a' se trouve à l'index {}".format(
            i + 1, index))

# Combien d'occurences de 'a' se trouvent dans la phrase ? 3
# Ou se trouve la première occurence de 'a' ? 11
# L'occurence numéro 2 de 'a' se trouve à l'index 20
# L'occurence numéro 3 de 'a' se trouve à l'index 23


print("Replacer les 'a' par des '*':")
phrase_masquee = phrase.replace("a", "*")
print(phrase)
print(phrase_masquee)

# Replacer les 'a' par des '*':
# cEcI est l'abc du b_a_ba
# cEcI est l'*bc du b_*_b*


#
# Exercice: Comptez le nombre de mots d'une phrase
#


def nb_mots1(phrase):
    return len(phrase.split(" "))

def nb_mots2(phrase):
    return phrase.count(" ") + 1



