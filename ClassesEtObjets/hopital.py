import datetime


class Personne:
    def __init__(self, nom, prenom, dN):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dN

    def afficher():
        print(self.nom, self.prenom, self.dateNaissance)

    def affecterService(self, service):
        service.ajouterPersonne(self)


class Medecin(Personne):
    def __init__(self, n, p, dN, specialite):
        super().__init__(n, p, dN)
        self.specialite = specialite

    def afficher(self):
        print(
            "D. " + self.nom,
            self.prenom,
            self.dateNaissance.strftime("%d %b %Y"),
            self.specialite,
        )


class Infermier(Personne):
    def __init__(self, n, p, dN):
        super().__init__(n, p, dN)


class Service:
    def __init__(self, nom, etage):
        self.nom = nom
        self.etage = etage
        self.personne = []
        self.materiel = []

    def afficher(self):
        print(self.nom, "etage", self.etage)

    def afficherPersonne(self):
        for i in self.personne:
            i.afficher()

    def ajouterPersonne(self, personne):
        self.personne.append(personne)

    def supprimerPersonne(self, personne):
        self.personne.remove(personne)
        del personne

    def ajouterMateriel(self, materiel):
        self.materiel.append(materiel)

    def supprimerMateriel(self, materiel):
        self.materiel.remove(materiel)
        del materiel


class Materiel:
    def __init__(self, nom, ref):
        self.nom = nom
        self.reference = ref

    def afficher(self):
        print(self.nom, self.reference)

    def affecterService(self, service):
        self.service = service
        service.ajouterMateriel(self)


class Hopital:
    def __init__(self, n, adresse):
        self.nom = n
        self.adresse = adresse
        self.services = []

    def afficher(self):
        print(self.nom, ",", self.adresse)

    def ajouterService(self, service):
        self.services.append(service)

    def supprimerService(self, service):
        self.services.remove(service)
        del service

    def afficherServices(self):
        for i in self.services:
            i.afficher()


h1 = Hopital("Nedir Mohamed", "Tizi Ouzou centre")
h1.afficher()

serv1 = Service("Pédiatrie", 1)

serv1.afficher()
h1.ajouterService(serv1)
h1.afficherServices()

m1 = Medecin("Ali", "Belkacem", datetime.datetime(1964, 3, 23), "Pédiatre")
serv1.ajouterPersonne(m1)

serv1.afficherPersonne()
