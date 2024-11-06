noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

#exercice 1
etudiant = zip(noms, scores)
#exercice 2
etudiant_20 = list(map(lambda x : (x[0], x[1] / 5), zip(noms, scores)))

#exercice 3
etudiant_bon = list(filter(lambda x : x[1] >= 17,  etudiant_20))

print(etudiant)
print(etudiant_20)
print(etudiant_bon)
#exercice 4
moyenne = sum(map(lambda x : x[1], etudiant_bon))/ len(etudiant_bon)
print(moyenne)