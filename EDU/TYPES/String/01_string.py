name = "Eliud Rojas"
desc = """
Hello my name is Eliud Rojas
but you can also call me Eliann
I'm a programming student at SENATI
"""
print(len(name))
print(name[0])
print(name[0:11])
print(name[5:])
print(name[:7])
print(name[:])



# --------------- REEMPLAZAR -----------------

# # Definir el texto original
# texto = "This is a test string."

# # Definir el diccionario de reemplazos
# reemplazos = {"i": "E", "s": "I"}

# # Mostrar el texto original
# print(f"El texto original es: {texto}")

# # Usar la función de reemplazar varios caracteres al mismo tiempo
# texto_modificado = reemplazar_varios(texto, reemplazos)

# # Mostrar el texto modificado
# print(f"El texto modificado es: {texto_modificado}")

# a = "This is a test string."
# b = {"i": "E", "s": "I"}
# for x, y in b.items():
#     a = a.replace(x, y)(x, y)
# print(a)



# --------------REEMPLAZAR TILDES U OTTHER-------------------

# DEFINIR FUNCION - QUITAR TILDE
# def Tild(s):
# TILD = (
#     ("á", "a"),
#     ("é", "e"),
#     ("í", "i"),
#     ("ó", "o"),
#     ("ú", "u"),
# )
# for a, b in TILD:
#     s = s.replace(a, b).replace(a.upper(), b.upper())
# return s



# ------------ Def Reemplazar_varios -----------------

# def reemplazar_varios(texto, diccionario):
#     # Recorre el diccionario y reemplaza cada clave por su valor
#     for clave, valor in diccionario.items():
#         texto = texto.replace(clave, valor)
#     return texto