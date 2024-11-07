class Personne():
    nom = "Humain 1"
    def saluer(self, nombre):
        for _ in range(0, nombre):
            print(f"Bonjour {self.nom}")

personne1 = Personne()
personne1.nom = "Alien 4"
personne1.saluer(3)
personne1.nom_de_famille = "Klux2000"
personne1.donnerprenom = lambda self: print(self.nom_de_famille)
print(personne1.nom_de_famille)

personne1.donnerprenom(personne1)

personne2 = Personne()
personne2.saluer(1)
