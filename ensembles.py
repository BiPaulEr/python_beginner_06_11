liste = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

ensemble = set(liste)  #{1, 2, 3, 4, 5}
print(ensemble)

ensemble_2 = {1, 3, 4, 5, 5, 5, 5}
print(ensemble_2)

print(3 in ensemble_2)
print(8 in ensemble_2)

ensemble_2.add(6)
print(ensemble_2) 
ensemble_2.add(5)
print(ensemble_2)

ensemble_2.remove(3)
#ensemble_2.remove(12)
print(ensemble_2)

equipe_a = {'Alice', 'Charles', 'Diane', 'Fabien'} #front_end
equipe_b = {'Bernard', 'Diane', 'Eloise', 'Fabien'} #back_end

exercice_1 = equipe_a & equipe_b
print(exercice_1)

exercice_2 = equipe_a | equipe_b
print(exercice_2)

exercice_3 = equipe_a ^ equipe_b
exercice_3 = (equipe_a | equipe_b) - (equipe_a & equipe_b)
print(exercice_3)

exercice_3_front_end = equipe_a - equipe_b
exercice_3_back_end = equipe_b - equipe_a
print(exercice_3_front_end)
print(exercice_3_back_end)

