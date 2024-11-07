nombres = [1, 2, 3, 4, 5]

carre = list(map(lambda x : x**2, nombres))
carre_impair = list(map(lambda x : x**2, filter(lambda x: x%2 , nombres)))
print(carre)
print(carre_impair)
  
carre_2 = [x**2 for x in nombres]
print(carre_2)

carre_impair_2 = [x**2 for x in nombres if x % 2 and x > 2]
print(carre_impair_2)
