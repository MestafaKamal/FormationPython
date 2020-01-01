# Les instructions qui permettent d'importer des fonctions ou bien des bibliothèques

# importer toutes les fonctions du fichier fonction.py
from fonctions import *

# Importer la fonction estPaire() du fichier fonction.py.
# from fonctions import estPaire

# Importer toute la bibliothèque math.
# C'est une bibliothèque standard qui contient des fonctions mathématiques
import math
import datetime

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

print("5! =", factorielle2(5))

print(multSix1(12))


personne1 = ["Kadi", "Dahbia"]
personne2 = ["Mellas", "Anais"]
personne3 = ["benramdane", "mustafa", "kamal"]
personne4 = ["Martin", "George", "Raymond", "Richard"]


print(initiales(personne3))


# D. KADI
# A. MELLAS
# M. K. BENRAMDANE
# G. R. R. MARTIN

# exercice
# Fonction qui calcule la factorielle d'un nombre
# def factorielle(a) ---> me renvoie la factorielle

# Fonction qui vérifie si un nombre est mutiple de 2 et 3
# en même temps

# Fonction qui affiche tous les nombres paires inférieurs à n donné
# affNbrPaire(n): elle me donne tous les nombres paires < n


nom1 = "Martin"
prenom1 = ["George", "Richard", "Raymond"]
date1 = "20-09-1948"


print(passwdGen1(nom1, prenom1, date1))


# MelAna01
# MarGeoRicRay20


# format() permet de formatter une chaine de caractère
# elle mets les paramètres qu'on lui donne dans les espaces réservés
# dans la chaine de caractère, selon l'ordre des paramètres.
# On utilise des indices pour forcer l'ordre de dépot des paramètre
nom = "Mon nom est {1}. Je suis né en {0}"
prenom = "karim"
mois = "Juin"
print(nom.format(23, mois))
