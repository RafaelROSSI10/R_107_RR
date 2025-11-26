import random

x = random.randint(0, 100)

print("J'ai choisi un nombre entre 0 et 100. Essaie de le deviner !")

essai = -1
compteur = 0

while essai != x:
    essai = int(input("Votre proposition : "))
    compteur += 1

    if essai < x:
        print("C'est plus grand.")
    elif essai > x:
        print("C'est plus petit.")
    else:
        print("Bravo ! Vous avez trouvé le nombre mystère.")
print("Nombre d'essais nécessaires :", compteur)