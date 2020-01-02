class Personne:
    cpt = 0

    def __init__(self, n, p, a):
        self.nom = n
        self.prenom = p
        self.age = a
        Personne.cpt = Personne.cpt + 1

    def afficherNom(self):
        print("Je m'appelle", self.nom, self.prenom)

    def modiferNom(self, nouveauNom):
        self.nom = nouveauNom

    def resume(self):
        Personne.cpt = 0


class Etudiant(Personne):
    def __init__(self, n, p, a, niveau):
        super().__init__(n, p, a)
        self.niveau = niveau


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


class Module:
    def __init__(self, nom, volume):
        self.nom = nom
        self.volume = volume

    def afficherMod(self):
        print(self.nom, "durant", self.volume, "d'heures")


p1 = Personne("ahmed", "karim", 23)
p2 = Personne("Mellas", "Anais", 20)
p3 = Personne("Kadi", "Dahbia", 24)

p1.age = 23

print(p1.nom, p1.prenom)
print(p2.nom)

p2.afficherNom()
p1.afficherNom()

p1.modiferNom("Malek")
p1.afficherNom()

print(p2.age)


print(Personne.cpt)

p1.resume()

print(Personne.cpt)


del p1

e1 = Etudiant("Elias", "Moussa", 24, "2AS")

print(e1.nom)

print(isinstance(p2, Etudiant))

m1 = Module("Python", 45)

ens1 = Enseignant("Kamal", "Mustafa", 24, "Ingénieur")
ens1.afficherNom()
ens1.affecterModules(m1)
ens1.afficherModules()

m1 = Module("Dev Web", 50)

ens1.affecterModules(m1)
ens1.afficherModules()

a = ens1.getDiplome()
print(a)
