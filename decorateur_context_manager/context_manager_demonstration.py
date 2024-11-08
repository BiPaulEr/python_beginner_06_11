class ContextIllustration():
    def __enter__(self):
        print("entering context")
        return "ceci est l'object renvoye par la mise enplace du contexte"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("leaving context")
        if (exc_type is None):
            print("Pas d'exception")
        else:
            print(f"{exc_type}, {exc_value}")
        return True

with ContextIllustration() as object_retourne_par_enter:
    print(object_retourne_par_enter)
    print("Je suis dans le contexte")
    raise Exception("ERREUR")

print("end")