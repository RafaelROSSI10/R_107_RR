# Déclaration de la liste
tab = [5, 2, 4, 8, 1, 3]

# Affichage de la liste initiale
print(tab)

# Algorithme de tri (style sélection avec affichage des phases)
for i in range(len(tab)):
    # Chercher le plus petit élément à partir de la position i
    min_index = i
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[min_index]:
            min_index = j

    # Si un élément plus petit est trouvé, on permute
    if min_index != i:
        tab[i], tab[min_index] = tab[min_index], tab[i]

    # Afficher la liste après chaque phase
    print(sorted(tab))
    print(tab)

