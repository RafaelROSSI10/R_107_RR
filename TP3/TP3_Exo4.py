n = int(input("Entrez un entier positif n : "))

print("Choisissez le type de boucle :")
print("1 - Boucle for")
print("2 - Boucle while")

choix = input("Votre choix (1 ou 2) : ")

fact = 1   # valeur initiale de la factorielle

if choix == "1":
    print("\nCalcul avec une boucle for :")
    for i in range(1, n + 1):
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")

elif choix == "2":
    print("\nCalcul avec une boucle while :")
    i = 1
    while i <= n:
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")
        i += 1

else:
    print("Choix invalide.")

print("\nLa factorielle de", n, "vaut :", fact)