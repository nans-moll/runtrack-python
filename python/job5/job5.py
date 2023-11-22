

# Boucle pour chaque lettre de l'alphabet en ordre décroissant
for lettre in range(ord('z'), ord('a')-1, -1):
    print(chr(lettre), end=' ')