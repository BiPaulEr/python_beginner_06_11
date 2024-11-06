age  = input("Entrez votre age svp ? ")
 
age = int(age)

if bool(age < 18):
    print("Mineur")
else:
    print("Majeur")

print("end")