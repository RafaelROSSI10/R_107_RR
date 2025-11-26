#Partie 1 :
# MostFrequent.py

liste = list(map(int, input("Entrez les éléments de la liste séparés par des espaces : ").split()))

frequences = {}

for elem in liste:
    if elem in frequences:
        frequences[elem] += 1
    else:
        frequences[elem] = 1

max_occurrence = 0
element_frequent = None

for elem in liste:  # Parcours dans l'ordre de la liste
    if frequences[elem] > max_occurrence:
        max_occurrence = frequences[elem]
        element_frequent = elem

print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({max_occurrence} x)")