def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verification_date(date_str):
    # Vérification du format
    if len(date_str) != 8 or not date_str.isdigit():
        return "Format incorrect ! La date doit contenir exactement 8 chiffres (jjmmaaaa)."

    # Extraction des parties
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])

    # Vérification du mois
    if mois < 1 or mois > 12:
        return f"Date incorrecte : le mois {mois} n'existe pas."

    # Détermination du nombre de jours dans le mois
    if mois in [1, 3, 5, 7, 8, 10, 12]:
        jours_dans_mois = 31
    elif mois in [4, 6, 9, 11]:
        jours_dans_mois = 30
    elif mois == 2:
        jours_dans_mois = 29 if est_bissextile(annee) else 28

    # Vérification du jour
    if jour < 1 or jour > jours_dans_mois:
        return f"Date incorrecte : le jour {jour} n'existe pas pour le mois {mois} en {annee}."

    return f"Date correcte : {jour:02d}/{mois:02d}/{annee}"

# -------------------------------
# Programme principal
date_saisie = input("Entrez une date au format jjmmaaaa : ")
print(verification_date(date_saisie))
