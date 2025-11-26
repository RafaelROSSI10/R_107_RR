def table_multiplication(nombre, limite=11):
    resultats = []
    for i in range(limite):
        resultats.append(nombre * i)

    # Affichage des résultats
    print(f"Vous cherchez la table de multiplication de quel nombre ?")
    for i in range(limite):
        print(f"{nombre} * {i} = {resultats[i]}")
# Programme principal
# On demande à l'utilisateur de saisir un nombre réel
try:
    n = float(input("Entrez un nombre réel : "))
    table_multiplication(n, 11)
except ValueError:
    print("Veuillez entrer un nombre valide.")