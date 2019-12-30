# Ce finchier contient la définition de différentes fonctions


# fonction qui affiche bonjour avec des paramètres
def afficherBonjour(a, b):
    print("Bonjour", a, b)
    return 1


# Fonction qui calcule la longueur d'une liste en utilisant une boucle
def longueur(a):
    # trouver la longueur de la liste a
    i = 0
    for x in a:
        i += 1
        # i = i+1
    return i


# Fonction qui calcule la longueur d'une liste
# en utilisant le dernier élément de la liste
def longueur1(a):
    return a.index(a[-1]) + 1


# Fonction qui indique si un nombre est paire ou pas
# Elle est implémentée avec IF ELSE
def estPaire(a):
    if isinstance(a, int) or isinstance(a, float):
        if a % 2 == 0:
            return True
        else:
            return False
    else:
        return False


# Fonction qui indique si un nombre est paire ou pas
# Elle est implémentée avec les expressions logiques
def estPaire1(a):
    if isinstance(a, int) or isinstance(a, float):
        return a % 2 == 0
    else:
        return False


# Fonction qui affiche tous les nombres paire inférieurs à un nombre donné.
def listerPaires(n):
    if n >= 0:
        for i in range(0, n):
            if estPaire(i):
                print(i)

