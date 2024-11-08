def simple_decorator(function):
    def wrapper(*args, **kwargs):
        print("Juste avant le call de la fonction")
        function(*args, **kwargs)
        print("Juste après le call de la fonction")
    return wrapper

@simple_decorator
def function_simple():
    print("Je suis dans la fonction simple")

@simple_decorator
def function_argument(nom):
    print(f"Je suis dans la fonction avec argument {nom}")

@simple_decorator
def function_argument_nominatif(nominatif = "TEST"):
    print(f"Je suis dans la fonction avec argument {nominatif}")

function_simple()

function_argument("OK")

function_argument_nominatif(nominatif = "OK ? ")

print("end")