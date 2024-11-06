chaine = "Bonjour Python"

liste_index = range(len(chaine) -1, -1, -1)

for i in liste_index:
    print(chaine[i])

for i in reversed(chaine):
    print(i)