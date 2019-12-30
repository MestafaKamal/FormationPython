admis = False
while admis == False:  # conditions
    moy = input("Donnez votre moyenne: ")

    # Les commandes try except permettent de gérer les erreurs
    try:
        # on essaye d'exécuter ce bloc
        moy = float(moy)
    except:
        # On traite l'erreur comme on veut.
        # On peut choisir d'ignorer l'erreur en mettant pass dans ce bloc.
        print("La valeur introduite est erronée")
        moy = 0

    if moy <= 20 and moy >= 0:
        if moy < 10:
            print("Ajourné(e)")
        else:
            print("Admis")
            admis = True
    else:
        print("Erreur!!")
