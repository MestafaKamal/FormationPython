x = input("Quel est votre moyenne? ")

# float() permet de trasformer une valeur en un nombre décimal
x = float(x)

if x >= 0 and x <= 20:

    # La boucle while permet de boucler sur un bloc tant que la condition est satisfaite.
    # On sort de la boucle la première fois que la condition est non-satisfaite
    while x < 10 and x >= 0:
        print("Vous devez refaire")
        x = input("Quel est votre moyenne maintenant? ")
        x = float(x)

    if x <= 20 and x >= 10:
        print("Felicitations!")
    else:
        print("erreur 1")
else:
    print("Erreur")
# exercice : optimiser le
# programme avec 1 seul imput

