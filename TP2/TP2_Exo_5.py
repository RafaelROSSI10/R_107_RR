nombre=int(input("Entrez un nombre entier :"))
if nombre == 0 :
    signe = "0"
elif nombre<0:
    signe="negatif"
else :
    signe="positif"

if nombre%2 ==0:
    paritee="pair"
else :
    paritee="impair"

print (f"le nombre est {signe} et {paritee}.")
