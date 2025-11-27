import random

def generer(nbr, vmin, vmax):
    tab = [random.randint(vmin, vmax) for _ in range(nbr)]
    return tab

def combienInferieur(table, vseuil):
    compteur = 0
    for val in table:
        if val < vseuil:
            compteur += 1
    return compteur

nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Valeur minimale (vmin) : "))
vmax = int(input("Valeur maximale (vmax) : "))

choix = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ").strip().lower()

if choix in ["oui", "o"]:
    vseuil = int(input("Précisez le seuil : "))
else:
    vseuil = 30

print(f"\nGénérer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print("Tableau généré trié :", tab)

total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")
