# Ce finchier contient la définition de différentes fonctions
import random
import datetime

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


def factorielle(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            f = 1
            for i in range(1, n + 1):
                f *= i
                # f = f * i

            return f
    else:
        return -1


def factorielle1(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            f = 1
            i = 1
            while i <= n:
                # f *= i
                f = f * i
                i += 1
            return f
    else:
        return -1


def factorielle2(n):
    if n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorielle2(n - 1)
    else:
        return -1


# Fonction qui indique si un nombre est multiple de six
# Elle est implémentée avec les expressions logiques
def multSix(a):
    if isinstance(a, int) or isinstance(a, float):
        return a % 6 == 0
    else:
        return False


# Fonction qui indique si un nombre est multiple de six
# Elle est implémentée avec les expressions logiques
def multSix1(a):
    if isinstance(a, int) or isinstance(a, float):
        return a % 2 == 0 and a % 3 == 0
    else:
        return False


def initiales(nomPersonne):
    # récupérer le nom de famille
    # nom = nomPersonne[0]

    # print(nom)

    chaine = ""
    # récupérer les prénoms
    for i in range(1, len(nomPersonne)):
        prenom = nomPersonne[i]
        # print(prenom[0])
        chaine = chaine + prenom[0].upper() + ". "

    chaine = chaine + nomPersonne[0].upper()
    # print(chaine)
    return chaine


nom = "Mellas"
prenom = "Anais"
date = datetime.datetime(2000, 1, 1)


def passwdGen(n, p, d):

    return n[0:3] + "." + p[0:3] + "." + str(d.day) + str(random.randint(0, 100))


print(passwdGen(nom, prenom, date))


# random est un module qui contient des foction de génération
# de nombres aléatoires
# random.randint() fonction est génère un entier aléatoire dans un intervalle.


def passwdGen1(n, p, d):
    print(nom)
    s = ""
    for i in p:
        s = s + i[0:3].capitalize() + "."

    # return n[0:3].capitalize() + "." + s + d[0:2] + str(random.randint(0, 100))
    return "{}.{}{}{}".format(n[0:3].capitalize(), s, d[0:2], random.randint(0, 100))


d = datetime.datetime(2018, 2, 12)

x = datetime.datetime.now()
print(x.strftime("On est le %d %B %Y à %H:%M:%S"))

if x < d:
    print("d n'est pas encore arrivé")
else:
    print("c'est une date passée")

