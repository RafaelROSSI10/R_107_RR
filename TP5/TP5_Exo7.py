import os.path
import datetime

# Lecture des noms de fichiers
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

# Vérification de l'existence et affichage des tailles
for fichier in [fichier1, fichier2]:
    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)
        print(f"Le fichier '{fichier}' existe et sa taille est de {taille} octets.")
    else:
        print(f"Le fichier '{fichier}' n'existe pas.")

# Comparaison des dates de modification si les deux existent
if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    modif1 = os.path.getmtime(fichier1)
    modif2 = os.path.getmtime(fichier2)

    date1 = datetime.datetime.fromtimestamp(modif1)
    date2 = datetime.datetime.fromtimestamp(modif2)

    if modif1 > modif2:
        print(f"\nLe fichier le plus récent est '{fichier1}', modifié le {date1}.")
    elif modif2 > modif1:
        print(f"\nLe fichier le plus récent est '{fichier2}', modifié le {date2}.")
    else:
        print("\nLes deux fichiers ont été modifiés à la même date.")
