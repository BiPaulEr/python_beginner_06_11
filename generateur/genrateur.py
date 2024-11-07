def compteur(debut, fin, pas):
    current_number = debut
    while current_number < fin:
        yield current_number*1
        yield current_number*-1
        current_number += pas

liste = []
for w in compteur(0, 10, 1):
    liste.append(w)

print(liste)
print("end")
