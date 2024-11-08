import time

def benchmark(function):
    def wrapper():
        temps = time.time_ns()
        function()
        temps_after = time.time_ns()
        temps_en_secondes = (temps_after - temps) * (10**-9)
        print(f"la {function.__name__} a mis {temps_en_secondes} de secondes.")
    return wrapper

@benchmark
def function_simple():
    print("Je suis dans la fonction simple")
    time.sleep(1)
    
@benchmark
def function_simple_2():
    print("Je suis dans la fonction simple 2")
    time.sleep(2)

function_simple()

function_simple_2()

print("end")