# Les instructions qui permettent d'importer des fonctions ou bien des bibliothèques

# importer toutes les fonctions du fichier fonction.py
from fonctions import *

# Importer la fonction estPaire() du fichier fonction.py.
# from fonctions import estPaire

# Importer toute la bibliothèque math.
# C'est une bibliothèque standard qui contient des fonctions mathématiques
import math


# Les appels des fonctions


# Appel de la fonction estPaire()
n = 24
print("Parité de ", n, " est ", estPaire1(n))

# Appel de la fonction listerPaires()
listerPaires(10)

# Appel de la fonction math.sqrt()
print("la racinde de 4 est ", math.sqrt(4))


# Appel de la fonction longueur1()
notes1 = [12.5, 8.5, "15", 13.75, 10, 16.25, 18]
print("longueur", longueur1(notes1))

# Appel de la fonction afficherBonjour
a = afficherBonjour("Ahmed", 2)
print(a)


# exercice
# Fonction qui calcule la factorielle d'un nombre
# def factorielle(a) ---> me renvoie la factorielle

# Fonction qui vérifie si un nombre est mutiple de 2 et 3
# en même temps

# Fonction qui affiche tous les nombres paires inférieurs à n donné
# affNbrPaire(n): elle me donne tous les nombres paires < n
