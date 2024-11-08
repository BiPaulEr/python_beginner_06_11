import math 

def read_value(data, key):
    return data.get(key, None)

def validate_data(value):
    if value is None:
        return None
    if not isinstance(value, (int, float)) or value < 0:
        return None
    return math.sqrt(value)

def process_sqrt_on_key(data, key):
    result = read_value(data, key)
    if result is None:
        return None
    return validate_data(result)

def log_result(data, key):
    result = process_sqrt_on_key(data, key)
    if result is None:
        print(f"Echec de sqrt pour la {key}")
    else:
        print(f"Le resultat de key est {result}")

if __name__ == "__main__":
    dictionnaire = {"cle1" : 9, "cle2" :25, "cle3": "Patate", "nombre_negatif": -1, "cle5": None}
    log_result(dictionnaire, "cle1")
    log_result(dictionnaire, "cle3")
    log_result(dictionnaire, "abscence_de_clef")
    log_result(dictionnaire, "nombre_negatif")