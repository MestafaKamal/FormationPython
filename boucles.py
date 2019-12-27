x = input("Quel est votre moyenne? ")
x = float(x)

if x >= 0 and x <= 20:
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

