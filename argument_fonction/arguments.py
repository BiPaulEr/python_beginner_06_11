def afficher_prix_total(prix_entree, prix_plat_principal, prix_dessert = 10, *args, **kwargs):
    total_prix = prix_entree + prix_plat_principal + prix_dessert + sum(args)
    print(f"Prix totale du repas est {total_prix}")
    for key, valeur in kwargs.items():
        print(f"{key} est asosicé à {valeur}")

prix_command = (3, 4, 6)
detail_command = {"client" : "john", "table" : 5}
afficher_prix_total(10, 20, 8, *prix_command, **detail_command)
afficher_prix_total(10, 20)