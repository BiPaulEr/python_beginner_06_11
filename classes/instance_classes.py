class Voiture():
    name = "Clio 2"
    def print(self):
        print(f"Je suis {self.name}")

voiture1 = Voiture()
voiture1.print()
voiture1.name = "Clio 2 Immatriculation 3"
voiture1.print()
print(voiture1.name)

voiture2 = Voiture()
print(type(voiture2))
voiture2.print()

Voiture.name