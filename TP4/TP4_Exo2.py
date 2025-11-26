# Demande le nombre d'étudiants
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

# Déclaration de la liste des notes
notes = []

# Remplissage de la liste avec vérification des bornes
for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:   # Vérification bornes
        print("Erreur : la note doit être comprise entre 0 et 20.")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    moyenne += note

# Calcul de la moyenne
moyenne = moyenne / nombreEtudiants

# Affichage des résultats
print(f"Moyenne de classe : {moyenne:.2f}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart:.2f}")