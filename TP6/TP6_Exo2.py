def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst1 = [0, 1, 2]
print("lst1 :", lst1)
print("type(lst1) :", type(lst1))
print("id(lst1) :", id(lst1))
lst2 = ajouter_elt(lst1, len(lst1))
print("lst2 :", lst2)
print("type(lst2) :", type(lst2))
print("id(lst2) :", id(lst2))

