nom1 = input("Entrez le nom de la première personne : ").strip()
prenom1 = input("Entrez le prénom de la première personne : ").strip()

nom2 = input("Entrez le nom de la deuxième personne : ").strip()
prenom2 = input("Entrez le prénom de la deuxième personne : ").strip()

ligne1 = prenom1.capitalize() + " " + nom1.upper()
ligne2 = prenom2.capitalize() + " " + nom2.upper()

if nom1.upper() < nom2.upper() or (nom1.upper() == nom2.upper() and prenom1.lower() < prenom2.lower()):
    print(ligne1)
    print(ligne2)
else:
    print(ligne2)
    print(ligne1)
