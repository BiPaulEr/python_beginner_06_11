class Visibility():
    def __init__(self, public, protected, private):
        self.public_variable = public
        self._protected_variable = protected #unique convention de nommage
        self.__private_variable = private

    def afficher(self):
        print(self.public_variable, self._protected_variable, self.__private_variable)

instance_visibility = Visibility("public", "protected", "private")
print(instance_visibility.public_variable)
print(instance_visibility._protected_variable)
#print(instance_visibility.__private_variable)
print(instance_visibility._Visibility__private_variable)

instance_visibility.afficher()