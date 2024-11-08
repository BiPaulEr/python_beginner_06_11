class Maison:
    def __init__(self, name, m2, prix):
        self.name = name
        self.m2 = m2
        self.prix = prix

    def nom(self):
        print(self, self.name, self.m2, self.prix)

class Villa(Maison):
    def __init__(self, sdb, name, m2, prix):
        self.sdb = sdb
        super().__init__(name, m2, prix)

    def nombre_de_salle_de_bains(self):
        print(f"Le nombre de salles de bain est {self.sdb}")

    def prix_par_salle_de_bains(self):
        prix_par_sdb = int(self.prix[:-1]) / self.sdb
        print(f"{prix_par_sdb}k")

class Manoir(Maison):
    pass

maison1 = Maison("Maison1", 30, "30k")
maison1.nom()

maison2 = Maison("Maison2", 40, "40k")
maison2.nom()

villa1 = Villa(5, "Villa 1", 130, "240k")       
villa1.nom()
villa1.nombre_de_salle_de_bains()
villa1.prix_par_salle_de_bains()
