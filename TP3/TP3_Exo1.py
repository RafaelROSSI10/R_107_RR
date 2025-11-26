#A
N = int(input("Entrez un entier naturel N : "))
somme = 0
for i in range(N + 1):
    somme += i
print("La somme des entiers de 0 à", N, "est :", somme)

#B
valeur = 0
while valeur != 100:
    valeur = int(input("Entrez un nombre (100 pour arrêter) : "))
print("Vous avez entré 100. Fin du programme.")

#C
moins_10 = 0
entre_10_15 = 0
plus_15 = 0

for i in range(10):
    valeur = float(input(f"Entrez la valeur n°{i+1} (entre 0 et 20) : "))

    while valeur < 0 or valeur > 20:
        print("Erreur : la valeur doit être comprise entre 0 et 20.")
        valeur = float(input(f"Entrez à nouveau la valeur n°{i+1} : "))

    if valeur < 10:
        moins_10 += 1
    elif valeur < 15:  # donc entre 10 inclus et < 15
        entre_10_15 += 1
    else:  # valeur >= 15
        plus_15 += 1

print("Nombre de valeurs < 10 :", moins_10)
print("Nombre de valeurs >= 10 et < 15 :", entre_10_15)
print("Nombre de valeurs >= 15 :", plus_15)

#D
X = int(input("Entrez une valeur X (supérieure à 1) : "))

# Initialisation
somme = 0
N = 0

while somme + N <= X:
    somme += N
    N += 1

N -= 1

print("Le plus grand N tel que la somme de 0 à N soit <= X est :", N)