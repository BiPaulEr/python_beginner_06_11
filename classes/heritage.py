class Animal():
    def __init__(self, name_animal):
        self.name = name_animal

    def print(self):
        print(f"Je suis un {self.name}")


    def print(self):
        print(" Je suis un embetteur d'humain")

class Chat(Animal):
    def __init__(self, type_de_miaulement, name_animal):
        self.miaou = type_de_miaulement
        super().__init__(name_animal)

    def miauler(self):
        print(self.miaou)

#animal1 = Animal("Animal 1")
#animal1.print()

#animal2 = Animal("Animal 2")
#animal2.print()

chat1 = Chat("MIAOU", "Chat 1")
chat1.print()
chat1.miauler()