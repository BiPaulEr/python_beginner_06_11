mots_de_passe = ["12345678", "password123", "abc123", "pythoniscool"]

for mdp in mots_de_passe:
    if len(mdp) < 8:
        print("Mot de passe faible trouvé")
        print(mdp)
        break