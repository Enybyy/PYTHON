busc = 20

for numero in range(7):
    # print(numero, numero * "hello")
    print(numero)
    if numero == busc:
        print("Numero encotrado: ", busc)
        break
else:
    print("El número no ha sido encontrado")

for char in "HELLO WORD":
    print(char)
