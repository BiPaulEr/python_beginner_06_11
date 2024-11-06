def double(x):
    return x * 2

def triple(x):
    return x * 3

def quadle(x):
    return x * 4

nombres = [1, 2, 3, 4]

print(list(map(lambda x : x*2, nombres)))  
print(list(map(lambda x : x*3, nombres)))  
print(list(map(lambda x : x*4, nombres)))  
print(list(map(lambda x : x*5, nombres)))  