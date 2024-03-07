# SET

# SET DEVUELVE DATOS SIN REPETIR
numbers_01 = {1, 1, 2, 1, 2, 3, 4}
print(numbers_01)
numbers_02 = [4, 5, 6]
numbers_02 = set(numbers_02)
print(numbers_02)

# UNE LOS DOS SET
print(numbers_01 | numbers_02)
# DEVUELVE EL DATO EL COMÚN
print(numbers_01 & numbers_02)
# DEVUELVE LA DIFERENCIA ENTRE numbers_01 y numbers_02
print(numbers_01 - numbers_02)
# DEVUELVE NUMERO QUE NO SE REPITAN numbers_01 y numbers_02
print(numbers_01 ^ numbers_02)
