# LISTAS
lista_01 = [1, 2, 3, 4, 5]  # LISTA
lista = (1, 2, 3, 4, 5)  # TUPLA
print(1, 2, 3, 4, 5)
print(*lista)

lista_02 = [7, 8]

print("HELLO", *lista_01, "WORD", *lista_02)


# DICCIONARIO:
p1 = {"x": 10, "y": "HELLO"}
p2 = {"y": 5}

newP = {**p1, "w": "Hola", **p2, "z": "WORD"}
print(newP)
