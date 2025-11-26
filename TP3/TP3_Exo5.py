debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")

elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.\n")

elif debut > fin:
    print("Attention ! le début de la location est après la fin ...\n")

else:
    heures_tarif1 = 0  # 1 euro/h (0-7 et 17-24)
    heures_tarif2 = 0  # 2 euros/h (7-17)

    for h in range(debut, fin):
        if (0 <= h < 7) or (17 <= h < 24):
            heures_tarif1 += 1
        else:
            heures_tarif2 += 1
    total = heures_tarif1 * 1.0 + heures_tarif2 * 2.0

    # Affichage conforme aux exemples
    print("Vous avez loué votre vélo pendant")
    if heures_tarif1 > 0:
        print(f"{heures_tarif1} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_tarif2 > 0:
        print(f"{heures_tarif2} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total à payer est de {total} euro(s).")