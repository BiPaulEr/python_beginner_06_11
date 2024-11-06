liste = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
test = list(enumerate(liste))
for valeur1, valeur2 in enumerate(liste):
    print("index " + str(valeur1))
    print("valeur " + str(valeur2))