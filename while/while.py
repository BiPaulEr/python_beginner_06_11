valeur_maximum = input("La valeur maximal ? ")
valeur_maximum = int(valeur_maximum)
valeur_de_depart = 1
somme = 0
while valeur_de_depart <= valeur_maximum:
    somme += valeur_de_depart
    valeur_de_depart += 1

print(somme)