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

