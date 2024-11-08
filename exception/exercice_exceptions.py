class TailleInvalideException(ValueError):
    pass


def convertion_en_entier(chaine):
    if not isinstance(chaine, str):
        raise TypeError(f"{chaine} is not str object")
    if len(chaine) < 5:
        raise TailleInvalideException(f"length of the cahine is {len(chaine)}")
    print("Convertion en cours :")
    try :
        result = int(chaine)
    except TypeError as te:
        print(f"Chaine de caractere is not convvertible : {te}")
    else:
        return result
    finally:
        print("Convertion terminé.")

if __name__ == "__main__":
    try:
        print(convertion_en_entier([]))
        print(convertion_en_entier("1.0"))
        print(convertion_en_entier("un"))
    except TypeError as ve:
        print(ve)
    except TailleInvalideException as ve:
        print(ve)