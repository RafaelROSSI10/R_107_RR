# Lecture de la chaîne de caractères
texte = input("Entrez un mot ou une phrase : ")

# Conversion en minuscules et suppression des caractères non alphabétiques
texte_epure = ""
for c in texte.lower():
    if c.isalpha():
        texte_epure += c

# Vérification du palindrome
if texte_epure == texte_epure[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
