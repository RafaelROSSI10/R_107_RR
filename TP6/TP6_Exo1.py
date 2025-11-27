L1 = [0] * 3
print(L1)          # [0, 0, 0]
print(type(L1))    # <class 'list'>
print(id(L1))      # Identifiant unique de la liste

for i, elem in enumerate(L1):
    print(f"Élément {i} : valeur={elem}, type={type(elem)}, id={id(elem)}")

L1[1] += 1
print(L1)          # [0, 1, 0]
print(type(L1))    # <class 'list'>
print(id(L1))      # Identifiant de la liste

for i, elem in enumerate(L1):
    print(f"Élément {i} : valeur={elem}, id={id(elem)}")

s = "machaine"
print(s, id(s), type(s))

for i, ch in enumerate(s):
    print(f"Caractère {i} : valeur={ch}, type={type(ch)}, id={id(ch)}")
