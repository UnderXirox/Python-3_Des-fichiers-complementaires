from random import choice, sample, shuffle

cartes = [chr(x) for x in range(0x1f0a1, 0x1f0af)]

print("Voici les cartes qui vous sont présentées: ", " ".join(cartes))

print("Vous en piochez une au hasard:", " ".join(choice(cartes)))
print("Vous en piochez cinq au hasard:", " ".join(sample(cartes, 5)))
shuffle(cartes)
print("Vous les mélangez:", " ".join(cartes))

