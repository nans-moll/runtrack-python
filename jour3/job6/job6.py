def check_positive_negative(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

# Exemples d'appels de la fonction
check_positive_negative(5)    # Affiche "positif"
check_positive_negative(-3)   # Affiche "negatif"
check_positive_negative(0)    # Affiche "nul"
