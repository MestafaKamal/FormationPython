print("Début du programme")
a = input("Quel est votre âge: ")
nom = input("Quel est vore nom? ")
if int(a) >= 18:
    print(nom + " vous êtes majeur")
    p = input("Quelle est la catégorie de votre permis? ")
    if int(p) == 1:
        print("Vous pouvez conduire une voiture")
    else:
        if int(p) == 2:
            print("Vous pouvez conduire un camion")
        else:
            print("Vous ne pouvez pas conduire")
    print("J'en ai marre")
else:
    print("Vous êtes mineur")
    print("Je suis à l'intérieure de else")
print("Fin du programme")

