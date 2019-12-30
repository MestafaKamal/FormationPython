# section définitions
def afficherBonjour(a, b):
    print("Bonjour", a, b)
    return 1


def longueur(a):
    # trouver la longueur de la liste a
    i = 0
    for x in a:
        i += 1
        # i = i+1
    return i


def longueur1(a):
    return a.index(a[-1]) + 1


def estPaire(a):
    if isinstance(a, int) or isinstance(a, float):
        if a % 2 == 0:
            return True
        else:
            return False
    else:
        return False


def estPaire1(a):
    if isinstance(a, int) or isinstance(a, float):
        return a % 2 == 0
    else:
        return False


def listerPaires(n):
    if n >= 0:
        for i in range(0, n):
            if estPaire(i):
                print(i)


# Les appels
n = 24
print("Parité de ", n, " est ", estPaire1(n))
listerPaires(10)


notes1 = [12.5, 8.5, "15", 13.75, 10, 16.25, 18]
print("longueur", longueur1(notes1))

a = afficherBonjour("Ahmed", 2)

print(a)

# exercice
# Fonction qui calcule la factorielle d'un nombre
# def factorielle(a) ---> me renvoie la factorielle

# Fonction qui vérifie si un nombre est mutiple de 2 et 3
# en même temps

# Fonction qui affiche tous les nombres paires inférieurs à n donné
# affNbrPaire(n): elle me donne tous les nombres paires < n
