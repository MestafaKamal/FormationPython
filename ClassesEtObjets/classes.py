# Dans ce script, nous définissons des classes qu'on instencie en objets afin de les
# manipulier.

# Une classe est une structure de donnée complexe construite à partir des types primitifs mais aussi
# à partir d'autres classes. Elle peut regrouper des méthodes et des attributs. Elle se comporte
# comme un moule à partir duquel on crée les objets.

# Un objet est une instence de cette classe. C'est un conteneur symblique d'un ensemble d'informations
# créé à partir d'un modèle qui est la classe.

# Les variables internes à une classe s'appellent des attribut de cette classe.
# Les fonctions internes à une classe s'appellent des méthodes de la classe.
# C'est à travers les méthodes qu'on intéragit avec une classe ou un objet de cette classe.

# Définiton de la classe Personne avec le mot clé class
class Personne:
    cpt = 0

    # la méthode __init__ est le constructeur de la classe Personne. Elle est exécutée
    # à chaque fois qu'un objet est créé. C'est dans cette méthode qu'on définit les attribut
    # de la classe ou qu'on les initialise.
    def __init__(self, n, p, a):
        self.nom = n
        self.prenom = p
        self.age = a
        Personne.cpt = Personne.cpt + 1

    def afficherNom(self):
        print("Je m'appelle", self.nom, self.prenom)

    # Méthode qui affiche le nom et le prénom de Personne.
    def afficher(self):
        print(self.nom, self.prenom)

    def modiferNom(self, nouveauNom):
        self.nom = nouveauNom

    def resume(self):
        Personne.cpt = 0


# Etudiant est une classe fille de la classe Personne. Elle hérite de tous ses attributs et méthodes.
# Donc pour un objet de la classe Etudiant, on peut utiliser toutes les méthodes de la classe Personne
# Une classe fille peut avoir des attribut supplémentaire, commme, dans ce cas, l'attribut  niveau
class Etudiant(Personne):

    # Dans la méthode __init__ d'une classe fille, on appelle le constructeur de la classe
    # mère en utilisant la méthode super(). Cela permet de créer un Etudiant en tant que Personne, pour
    # ensuite lui ajouter des attributs supplémentaires
    def __init__(self, n, p, a, niveau):
        super().__init__(n, p, a)
        self.niveau = niveau


# Enseignant est également un classe fille de la classe personne. Comme Etudiant, elle hérite de tous
# les attributs et méthodes de la classe Personne.
class Enseignant(Personne):
    def __init__(self, n, p, a, d):
        super().__init__(n, p, a)
        self.diplome = d
        self.modules = []

    def affecterModules(self, m):
        if isinstance(m, Module):
            self.modules.append(m)
        else:
            print("Veuillez ajouter un module")

    def afficherModules(self):
        print("Les module de M.", self.nom, "sont: ")
        for i in self.modules:
            i.afficherMod()

    def getDiplome(self):
        return self.diplome


# Dafinition de la classe Module
class Module:
    def __init__(self, nom, volume):
        self.nom = nom
        self.volume = volume

    # Le paramètre self doit figurer dans toutes les méthodes. Il re présente l'objet
    # à partir duquel la méthode est appelée. Il est toujours placé en premier et cela dans
    # le cas où nous avons d'autres paramètres ou pas.
    def afficherMod(self):
        print(self.nom, "durant", self.volume, "d'heures")


# création d'objets de la classe Personne. Les paramètres passés dans le constructeur Personne()
# sont passés à la méthode __init__ de la classe Personne
p1 = Personne("ahmed", "karim", 23)
p2 = Personne("Mellas", "Anais", 20)
p3 = Personne("Kadi", "Dahbia", 24)

# Modifier un attribut directement.
p1.age = 23

# Accès à des attributs des objets
print(p1.nom, p1.prenom)
print(p2.nom)

# Appel des méthodes définies dans les classes.
# Elles s'appliquent sur les objets cités dans l'appel.
p2.afficherNom()
p1.afficherNom()

p1.modiferNom("Malek")
p1.afficherNom()

print(p2.age)


print(Personne.cpt)

p1.resume()

print(Personne.cpt)


# Supprimet l'objet p1
del p1

# Instencier un objet Etudiant.
e1 = Etudiant("Elias", "Moussa", 24, "2AS")

print(e1.nom)

print(isinstance(p2, Etudiant))


# Instencier un objet Module.
m1 = Module("Python", 45)

# Instencier un objet Enseignant
ens1 = Enseignant("Kamal", "Mustafa", 24, "Ingénieur")
ens1.afficherNom()
ens1.affecterModules(m1)
ens1.afficherModules()

m1 = Module("Dev Web", 50)

ens1.affecterModules(m1)
ens1.afficherModules()

a = ens1.getDiplome()
print(a)

ens1.afficher()
