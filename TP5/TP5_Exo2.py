notes = []
coefficients = []

for i in range(1, 6):
    note = float(input(f"Entrez la note du module {i} : "))
    coeff = int(input(f"Entrez le coefficient du module {i} : "))

    notes.append(note)
    coefficients.append(coeff)

total_points = sum(notes[i] * coefficients[i] for i in range(5))
total_coeffs = sum(coefficients)
moyenne = total_points / total_coeffs

admis = moyenne > 10 and all(note >= 8 for note in notes)

# Affichage des résultats
print(f"\nMoyenne générale : {moyenne:.2f}")
if admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
