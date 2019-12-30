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


notes1 = [12.5, 8.5, "15", 13.75, 10, 16.25, 18]
notes2 = [14, 15.5, 7.5, 14, 18, 10]
listeMoyenne = []

a = moyenne(notes1)

print("La moyenne des notes est", a)
print("La moyenne des notes est", moyenne(notes2))

