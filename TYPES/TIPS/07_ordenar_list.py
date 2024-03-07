numbers = [54, 21, 894, 12, 3, 15, 8, 1, 2, 7, 84]

# NUMEROS ORDENADOS
numbers.sort()
print("Números ordenados:", numbers)
# UMEROS REVERSE
numbers.sort(reverse=True)
print("Números ordenados al revés:", numbers)
# NUMEROS ORDENADOS
numbers_01 = sorted(numbers)
print(numbers_01)


users_00 = [
    ["RSNJ", 3],
    ["IGSA", 1],
    ["POIO", 7],
    ["HGFF", 5]
]

users_01 = [
    ["RSNJ", 3],
    ["IGSA", 1],
    ["POIO", 7],
    ["HGFF", 5]
]


def ordena(ordenar):
    return ordenar[1]


# ORDENAR "NEeD FUN"
users_00.sort(key=ordena)
print(users_00)

# ORDENANDO LISTA WHIT "LAMBDA":
users_01.sort(key=lambda el: el[1])
print(users_01)
