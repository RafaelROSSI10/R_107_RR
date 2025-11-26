# Taille maximale des vecteurs
nMax = 3

# Déclaration des listes
v1 = []
v2 = []

# Demande de la taille effective
n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
while n < 1 or n > nMax:
    print("Erreur : taille non valide.")
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

# Saisie du premier vecteur
print("Saisie du premier vecteur :")
for i in range(n):
    val = int(input(f"v1[{i}] = "))
    v1.append(val)

# Saisie du second vecteur
print("Saisie du second vecteur :")
for i in range(n):
    val = int(input(f"v2[{i}] = "))
    v2.append(val)

# Calcul du produit scalaire
produit = 0
for i in range(n):
    produit += v1[i] * v2[i]

# Affichage du résultat
print(f"Le produit scalaire de v1 par v2 vaut {produit:.1f}")