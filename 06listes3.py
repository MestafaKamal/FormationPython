notes = [12.5, 8.5, 15, 13.75, 10, 16.25, 18]

s = 0
for x in notes:
    # s = s + x
    s += x

# traiter le cas où la liste est vide
if len(notes) > 0:
    print("La moyenne est", s / len(notes))
else:
    print("Il n'y a pas de notes")

notes2 = [14, 15.5, 7.5, 14, 18, 10]

s = 0
for x in notes2:
    # s = s + x
    s += x

# traiter le cas où la liste est vide
if len(notes2) > 0:
    print("La moyenne est", s / len(notes))
else:
    print("Il n'y a pas de notes")


# solution générale, et non recommandée
# try:
#    print("La moyenne est", s / len(notes))
# except:
#    print("y a pas de notes")

# Faire un programme qui calcule la moyenne des notes
# Afficher le résultat suivant:

# La moyenne est 00.0


# Pour calculer la moyenne, il faut fairela somme des notes,
#  et qu'on divise par le nombre des modules.
# moyenne = (la somme des notes)/(le nombre des modules)
