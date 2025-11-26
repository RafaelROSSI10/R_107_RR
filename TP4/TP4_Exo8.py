# tp4exo8.py
etudiant1 = {
    "firstname": "titi",
    "name": "toto",
    "promo": 2022,
    "group": 202
}


print(f"Votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', "
      f"vous faites partie de la promo '{etudiant1['promo']}' et votre groupe est '{etudiant1['group']}'\n")

print("Les clés du dictionnaire sont :")
for cle in etudiant1.keys():
    print("-", cle)

print("\nLes valeurs du dictionnaire sont :")
for valeur in etudiant1.values():
    print("-", valeur)

print("\nLes tuplets du dictionnaire sont :")
for couple in etudiant1.items():
    print("-", couple)

etudiant2 = {
    "firstname": "tutu",
    "name": "tata",
    "promo": 2023,
    "group": 102
}

binome = {
    "poste1": etudiant1,
    "poste2": etudiant2
}

print("\nLes étudiants formants le binôme sont :")
for identifiant, etudiant in binome.items():
    print(f"- L'étudiant {etudiant['name']} {etudiant['firstname']} du groupe {etudiant['group']}")
