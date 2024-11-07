print([x for x in range(0, 12)])
gen = (x for x in range(0, 12))

for i in gen:
    print(i)