caracteres = input("Saississez des caractères: ")
# Exemple avec aA019éà@#`{

for caractere in caracteres:
    print("Le caractère {} a pour ordinal {}".format(caractere, ord(caractere)))


# Le caractère a a pour ordinal 97
# Le caractère A a pour ordinal 65
# Le caractère 0 a pour ordinal 48
# Le caractère 1 a pour ordinal 49
# Le caractère 9 a pour ordinal 57
# Le caractère é a pour ordinal 233
# Le caractère à a pour ordinal 224
# Le caractère @ a pour ordinal 64
# Le caractère # a pour ordinal 35
# Le caractère ` a pour ordinal 96
# Le caractère { a pour ordinal 123


nombres = input("saisissez des nombres, séparés par un espace: ")
# Exemple avec 123 233 42 420 4200 4242 42000 424242

for nombre in nombres.split(" "):
    try:
        print("Le caractère d'ordinal {} est {}".format(nombre,
                                                        chr(int(nombre))))
    except:
        print("Le nombre {} n'est pas un ordinal valide".format(nombre))

# Le caractère d'ordinal 123 est {
# Le caractère d'ordinal 233 est é
# Le caractère d'ordinal 42 est *
# Le caractère d'ordinal 420 est Ƥ
# Le caractère d'ordinal 4200 est ၨ
# Le caractère d'ordinal 4242 est ႒
# Le caractère d'ordinal 42000 est ꐐ
# Le caractère d'ordinal 424242 est 񧤲


print("Et maintenant, voici quelques caractères non usuels:")
print(chr(0x2318),
      chr(0x2704),
      chr(0x2764),
      chr(0x265b),
      chr(0x2620),
      chr(0x2622),
      chr(0x1f053),
      chr(0x1f084),
      chr(0x1f0d1))

# ⌘ ✄ ❤ ♛ ☠ ☢ 🁓 🂄 🃑
