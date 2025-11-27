# Programme Palindrome.py adapté pour l'exercice sur T[100]

# 1. Lecture de la chaîne
T = input("Entrez une chaîne de caractères (max 100) : ")

# 1. Calcul de la taille de la chaîne (sans utiliser len)
taille = 0
for c in T:
    taille += 1

print(f"Taille de la chaîne : {taille}")

# 2. Calcul du pourcentage de voyelles
voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
for c in T:
    if c in voyelles:
        nb_voyelles += 1

pourcentage_voyelles = (nb_voyelles / taille) * 100 if taille > 0 else 0
print(f"Pourcentage de voyelles : {pourcentage_voyelles:.2f}%")

mot = "wagon"
pos = -1
for i in range(taille - len(mot) + 1):  # parcours manuel
    j = 0
    while j < len(mot) and T[i + j].lower() == mot[j]:
        j += 1
    if j == len(mot):
        pos = i
        break

if pos != -1:
    print(f'La sous-chaîne "{mot}" apparaît à la position {pos}.')
else:
    print(f'La sous-chaîne "{mot}" n\'apparaît pas.')

occurrences = 0
for i in range(taille - len(mot) + 1):
    j = 0
    while j < len(mot) and T[i + j].lower() == mot[j]:
        j += 1
    if j == len(mot):
        occurrences += 1

print(f'Nombre d\'occurrences de "{mot}" : {occurrences}')
