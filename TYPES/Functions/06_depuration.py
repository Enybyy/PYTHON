
def large(text):
    contador = 0
    for char in text:
        contador += 1
    return contador


l = large("HELLO WORD")
print(l)


# DEF WHIT LEN
def larg(test):
    contar = len(test)
    print(contar)


larg("hola")


# CONTAR
numeros = [1, 2, 3, 4, 5]
cantidad = len(numeros)
print(cantidad)

# CONTAR
numeros = [1, 2, 3, 4, 5]
contador = 0
for numero in numeros:
    numero = numero + numero
print(numero)


# CONTAR
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero * 2)


numeros = [1, 2, 3, 4, 5]
contador = 0
for numero in numeros:
    contador += numero
print(contador)
