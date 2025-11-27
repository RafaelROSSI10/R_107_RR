def ajouter_elt(lst=[0,1,2], elt=3):
    print("id(lst) :", id(lst))
    lst.append(elt)
    return lst

print(ajouter_elt())
print(ajouter_elt())
print(ajouter_elt())

def ajouter_carac(chaine="machaine", carac="!"):
    nouvelle_chaine = chaine + carac
    print("id(chaine) :", id(chaine))
    print("id(nouvelle_chaine) :", id(nouvelle_chaine))
    return nouvelle_chaine

print(ajouter_carac())
print(ajouter_carac())
print(ajouter_carac())

