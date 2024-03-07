users_00 = [
    ["RSNJ", 3],
    ["IGSA", 1],
    ["POIO", 7],
    ["HGFF", 5]
]

# map
# users = ["expresion" for "item" in "items"]
users_01 = [users_02[0] for users_02 in users_00]
users_01.sort()
print(users_01)

# filter
# users = ["expresion" for "item" in "items" if "fil"]
users_01 = [users_02 for users_02 in users_00 if users_02[1] > 3]

# FILTRAR Y TRANSFORMAR
users_01 = [users_02[0] for users_02 in users_00 if users_02[1] > 3]
print(users_01)

# MAP
users_01 = list(map(lambda users_02: users_02[1], users_00))
print(users_01)

# FILTER
users_01 = list(filter(lambda users_02: users_02[1] > 3, users_00))
print(users_01)
