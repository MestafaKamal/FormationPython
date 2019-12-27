admis = False
while admis == False:  # conditions
    moy = input("Donnez votre moyenne: ")
    try:
        # on essaye d'exécuter ce bloc
        moy = float(moy)
    except:
        # On traite l'erreur
        print("La valeur introduite est erronée")
        moy = 0

    if moy <= 20 and moy >= 0:
        if moy < 10:
            print("Ajourné")
        else:
            print("Admis")
            admis = True
    else:
        print("Erreur!!")
