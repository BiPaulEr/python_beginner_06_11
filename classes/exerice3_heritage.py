class Animal:
    def parler(self):
        print("Je suis un animal")
    
    def discuter(self):
        print("Je suis un animal")
    
    def crier(self):
        print("JE SUIS UN ANIMAL")

class Chien(Animal):
    def parler(self):
        print("Je suis un chien mais aussi....")
        super().parler()
    
    def crier(self):
        print("JE SUIS UN CHIEN")
    
    def aboyer(self):
        print("WHOUAF")

    
chien = Chien()
chien.parler()
chien.discuter()
chien.crier()
chien.aboyer()

