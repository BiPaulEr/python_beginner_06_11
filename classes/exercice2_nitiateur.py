class Voiture():
    def __init__(self, marque, model):
        self.marque = marque
        self.modele = model

    def afficher(self):
        print(self.marque, self.modele)

voiture1 = Voiture("Citroen", "C2")
voiture1.afficher()
