# Lecture de la somme
somme = int(input("Entrez une somme d'argent (valeur entière) : "))

# Décomposition en billets et pièces
billet100 = somme // 100
reste = somme % 100

billet50 = reste // 50
reste = reste % 50

billet10 = reste // 10
reste = reste % 10

piece2 = reste // 2
reste = reste % 2

piece1 = reste

# Affichage du résultat
print("\nDécomposition de la somme :")
print(f"Billets de 100 : {billet100}")
print(f"Billets de 50  : {billet50}")
print(f"Billets de 10  : {billet10}")
print(f"Pièces de 2    : {piece2}")
print(f"Pièces de 1    : {piece1}")
