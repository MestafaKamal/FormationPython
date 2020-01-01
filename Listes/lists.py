liste = ["Tomate", "Oignon", "Patate", "Aubergine", "2"]
print(liste)
print(" le troisième élément est " + liste[2])
print(len(liste))
print("la longueur de la liste est " + str(len(liste)))
print(liste[-2])
print(liste[1:4])
print(liste[-3:-1])
# insérer à la fin de la liste
liste.append("Poivron")
print(liste)
# insérer à la quatrième position (indice 3)
liste.insert(3, "Fèves")
print(liste)
# retrouver l'indice d'un élément
print("L'indice de 'Oignon' est " + str(liste.index("Oignon")))
# supprimer un élément
liste.remove("Oignon")
print(liste)
# supprimer avec indice
del liste[0]
print(liste)
# supprimer la queue de liste
a = liste.pop()
print(a)
print(liste)


# trier la liste
liste.sort()
print(liste)
# inverser l'ordre de la liste
liste.reverse()
print(liste)

# copier une liste dans une autre
liste2 = list(liste)
liste2 = ["Mardi", "Mercredi", 4]

liste3 = liste + liste2
print(liste3)


for x in liste3:
    try:
        print(x[0] + ".")
    except:
        pass

print("boucle avec range")
print(liste3)
for i in range(2, 6):
    print(liste3[i])


print(liste2)
for i in liste2:
    #    print(i)
    if i == "Mardi":
        print("oui mardi existe")
        break
        # beark permet de faire un arrêt forcé de la boucle.


# vider la liste
liste.clear()
print(liste)

# https://github.com/MestafaKamal/FormationPython

