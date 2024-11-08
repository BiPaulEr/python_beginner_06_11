class Instrument:
    """
    Classe de base représentant un instrument.
    """
 
    def jouer(self):
        """
        Méthode à redefinir dans les sous-classes pour jouer de l'instrument.
        """
        raise NotImplementedError("Cette méthode doit être redéfinie dans les sous-classes")
 
class Guitare(Instrument):
    """
    Classe représentant une guitare, héritant de la classe Instrument.
    """
 
    def jouer(self):
        """
        Affiche un message indiquant que la guitare joue.
        """
        print("Je joue de la guitare")
 
class Piano(Instrument):
    """
    Classe représentant un piano, heritant de la classe Instrument.
    """
 
    def jouer(self):
        """
        Affiche un message indiquant que le piano joue.
        """
        print("Je joue du piano")

class Saxophone(Instrument):
    """
    Classe représentant un saxo, heritant de la classe Instrument.
    """
 
    def jouer(self):
        """
        Affiche un message indiquant que le piano joue.
        """
        print("Je joue du saxo") 

def faire_jouer(instruments):
    """
    Prend une liste d'instruments et appelle sa methode jouer pour chaque instrument.
    """
    for instrument in instruments:
        instrument.jouer()
 
# Création d'instances de Guitare et Piano
guitare = Guitare()
piano = Piano()
saxo = Saxophone()
 
# Utilisation de la fonction faire_jouer avec des instances de Guitare et Piano dans une liste
instruments = [guitare, piano, saxo]
faire_jouer(instruments)
