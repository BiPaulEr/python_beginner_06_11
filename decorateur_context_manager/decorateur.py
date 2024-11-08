def simple_decorator(function):
    def wrapper():
        print("Juste avant le call de la fonction")
        function()
        print("Juste après le call de la fonction")
    return wrapper

def function_simple():
    print("Je suis dans la fonction simple")

def function_simple_2():
    print("Je suis dans la fonction simple 2")

function_simple = simple_decorator(function_simple)
function_simple_2 = simple_decorator(function_simple_2)

function_simple()

function_simple_2()



print("end")