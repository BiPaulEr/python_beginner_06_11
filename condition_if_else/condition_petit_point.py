listes = ["paul","martin", "ernest"]
test = list(enumerate(listes))
#[(0, 'martin'), (1, 'paul'), (2, 'ernest')]

for index in range(0, 3):
    listes[index] = listes[index].upper()

print(listes)
