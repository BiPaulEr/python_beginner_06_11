file = open("./data.txt")
try:
    for line in file:
        print(line)
finally:
    file.close()

with open("./data.txt") as file:
    for line in file:
        print(line)