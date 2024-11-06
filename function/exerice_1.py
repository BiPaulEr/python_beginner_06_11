def calcule_prix_tva(prix_ht : float, tva : float) -> float:
    prix_ttc = prix_ht * (tva / 100) + prix_ht
    return prix_ttc

prix_ttc = calcule_prix_tva(100, 20)
print(prix_ttc)

prix_ttc = calcule_prix_tva(100, 10)
print(prix_ttc)
