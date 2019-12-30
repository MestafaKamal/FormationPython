# Programme d'introduction des variables, conditions et expressions logiques.

print("Début du programme")

# Definition de la variable a. input() permet de lire une valeur à partir du clavier.
a = input("Quel est votre âge: ")
nom = input("Quel est vore nom? ")

# la commande if permet de tester si une condition est satisfaite.
# int(a) permet de trasformer la caractère a qui est lu en un nombre entier.
if int(a) >= 18:
    # Si la condition est satisfaite, on exécute ce bloc.

    # print() permet d'afficher à l'écran
    print(
        nom + " vous êtes majeur"
    )  # le + permet de cancaténer deux chaines de caractères
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
    # Si la condition n'est pas satisfaite, on exécute ce bloc.
    print("Vous êtes mineur")
    print("Je suis à l'intérieure de else")
print("Fin du programme")

