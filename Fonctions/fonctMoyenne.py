# Ce fichier contient la définition de la fonction moyenne() et qui calcule la
# moyenne arithmétique d'une liste de nombres.


def moyenne(a):
    if isinstance(a, list):
        s = 0
        for x in a:
            # s = s + x
            if isinstance(x, int) or isinstance(x, float):
                s += x
            else:
                pass

        # traiter le cas où la liste est vide
        if len(a) > 0:
            # print("La moyenne des notes est", s / len(a))
            return s / len(a)
        else:
            print("Il n'y a pas de notes")
    else:
        print("Ce n'est pas une liste")


# Utilisation de la fonction moyenne() sur des listes.


notes1 = [12.5, 8.5, "15", 13.75, 10, 16.25, 18]
notes2 = [14, 15.5, 7.5, 14, 18, 10]
notes3 = [13.75, 10, 16.25, 18]
listeMoyenne = []

a = moyenne(notes1)

print("La moyenne des notes est", a)
print("La moyenne des notes est", moyenne(notes2))

listeMoyenne.append(moyenne(notes1))
listeMoyenne.append(moyenne(notes2))
listeMoyenne.append(moyenne(notes3))

print(listeMoyenne)

print("Moyenne de la classe", moyenne(listeMoyenne))

