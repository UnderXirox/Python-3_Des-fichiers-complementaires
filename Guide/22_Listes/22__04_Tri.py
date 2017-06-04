phrase = "Ah! La phrase à trier a été déclarée."

phrase = phrase.replace("!", "").replace(".", "")

mots = phrase.split()

print("Mots non triés: {}".format(mots))

mots.sort()

print("Tri simple: {}".format(mots))

mots.sort(key=str.lower)

print("Casse traitée: {}".format(mots))

translation = str.maketrans(
   "àäâéèëêïîöôùüûÿŷç_-",
   "aaaeeeeiioouuuyyc  ",
   "#~.?,;:!")

print("Dictionnaire de remplacement", translation)

def transformation(x):
    return x.lower().translate(translation)

mots.sort(key=transformation)

print("Accents traités: {}".format(mots))

