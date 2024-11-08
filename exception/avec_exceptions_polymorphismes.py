import math 

class ValueNegativeError(Exception):
    pass

def read_value(data, key):
    value = data.get(key, None)
    if value is None:
        raise ValueError(f"value found in dictionnaire for {key} is not find in {data.keys()}")
    return value

def validate_data(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"type of value {value} is not int or float")
    if value < 0:
        raise ValueNegativeError(f"value is negative : {value}")
    return math.sqrt(value)

def process_sqrt_on_key(data, key):
    result = read_value(data, key)
    return validate_data(result)

def log_result(data, key):
    print(f"BEGIN : processing {key}")
    try: 
        result = process_sqrt_on_key(data, key)      
    except TypeError as type_error:
        print(type(type_error))
        print(f"{type_error}")
        data.pop(key)
        print("Element est alors supprimé du dictionnaire")
    except ValueNegativeError as negative:
        print(type(negative))
        print(f"{negative}")
        data[key] = abs(data[key])
        print("Element est tranformer par la valeur absolue")
    except Exception as e:
        print(type(e))
        print(f"{e}")
  
    else:
        print(f"for {key} value of sqrt is {result}")
    finally:
        print(f"END : processing {key}")


if __name__ == "__main__":
    dictionnaire = {"cle1" : 9, "cle2" :25, "cle3": "Patate", "nombre_negatif": -1, "cle5": None}
    try:
        log_result(dictionnaire, "cle1")
        log_result(dictionnaire, "cle3")
        log_result(dictionnaire, "abscence_de_clef")
        log_result(dictionnaire, "nombre_negatif")
    except Exception as e:
        print(f"{e}")