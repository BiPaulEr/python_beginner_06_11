def repeat_decorator(nombre_de_repetition):
    def repeat(function):
        def wrapper():
            for _ in range(0, nombre_de_repetition):      
                function()     
        return wrapper
    return repeat

@repeat_decorator(1000)
def function_simple():
    print("Je suis dans la fonction simple")

function_simple()

print("end")