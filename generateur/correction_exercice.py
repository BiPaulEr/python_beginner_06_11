print("Exercice 1")
def generateur_pair(n):
    for i in range(0, n, 2):
        yield i

for i in generateur_pair(10):
    print(i)

print("Exercice 2")
def generateur_carre(n):
    for i in range(1, n+1):
        yield i**2

for i in generateur_carre(5):
    print(i)

print("Exercice 3")
def fibonacci(n):
    a , b = 0, 1 
    for _ in range(0, n):
        yield a
        a, b = b, a+b

def fibonacci_(n):
    a = 0
    b = 1 
    for i in range(0,n):
        yield a
        tmp = a
        a = b
        b = tmp + b

for i in fibonacci(10):
    print(i)