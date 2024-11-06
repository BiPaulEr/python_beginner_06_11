liste_index = range(1, 51, 1)
somme = 0
for i in liste_index:
    if i % 2 == 1:
        somme += i
print(somme)

somme = 0
for i in range(1, 51, 2):
    somme += i
print(somme)

print(sum(range(1, 51, 2)))