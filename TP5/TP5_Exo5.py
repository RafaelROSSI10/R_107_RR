# Lecture des données
heures = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Calcul du salaire
salaire = 0

if heures <= 160:
    salaire = heures * salaire_horaire
elif heures <= 200:
    # 160 premières heures au tarif normal
    salaire = 160 * salaire_horaire
    # heures entre 161 et heures au tarif +25%
    salaire += (heures - 160) * (salaire_horaire * 1.25)
else:
    # 160 premières heures au tarif normal
    salaire = 160 * salaire_horaire
    # 40 heures suivantes (161 à 200) au tarif +25%
    salaire += 40 * (salaire_horaire * 1.25)
    # heures au-delà de 200 au tarif +50%
    salaire += (heures - 200) * (salaire_horaire * 1.5)

# Affichage du résultat
print(f"\nLe salaire de l'ouvrier est : {salaire:.2f} €")
