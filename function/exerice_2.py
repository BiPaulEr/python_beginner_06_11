def conserver_que_les_int(donnees):
    liste = []
    for element in donnees:
        if (isinstance(element, int)):
            liste.append(element)
    return liste


def nettoyer_donnees(donnees):
    liste = []
    for element in donnees:
        if (element is not None):
            liste.append(element)
    return liste

def filtrer_donnees(donnee):
    liste = []
    for element in donnee:
        if (element >= 0 and element <= 10):
            liste.append(element)
    return liste

def analyser_donnee(donnee):
    liste = nettoyer_donnees(donnee)
    liste = filtrer_donnees(liste)
    return liste

liste = [5, 15, None, 10, 20]
liste_nettoye = nettoyer_donnees(liste)
liste_nettoye_2 = conserver_que_les_int(liste)

liste_filtre = filtrer_donnees(liste_nettoye)
liste_filtre_2 = analyser_donnee(liste)
print("end")