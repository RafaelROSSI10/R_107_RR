import unicodedata
import string
def supprimer_accents(texte):
    texte_normalise = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(
        c for c in texte_normalise if unicodedata.category(c) != 'Mn'
    )
    return texte_sans_accents
def nettoyer_texte(texte):
    texte = supprimer_accents(texte)
    texte = texte.lower()
    caracteres_a_supprimer = string.punctuation + string.whitespace
    texte_nettoye = ''.join(
        c for c in texte if c not in caracteres_a_supprimer
    )
    return texte_nettoye
def est_palindrome(texte):
    texte_nettoye = nettoyer_texte(texte)
    return texte_nettoye == texte_nettoye[::-1]
phrase = input("Entrez un mot ou une phrase : ")
if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
