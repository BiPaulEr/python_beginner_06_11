prenoms = ["seb", "martin", "paul", "ernest" ]
noms = ["DUPONT", "MARTIN", "AIGOUY", "" ]
ages = [12, 23, 54, 90]

print(list(zip(prenoms, noms, ages)))

print(list(enumerate(zip(prenoms, noms, ages))))

for index, prenom, nom, age in enumerate(zip(prenoms, noms, ages)):
    prenoms[index] = prenom.upper()
    print(prenom, nom, age)
