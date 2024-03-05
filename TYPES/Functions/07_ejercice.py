# ELIMINAR ESPACIO EN BALCNO
# def del_space(text):
#     new_text = ""
#     for char in text:
#         if char != " ":
#             new_text += char
#     return new_text
# del_espace("Hola que tal")


# DEFINIR FUNCION PARA ELIMINAR ESPACIOS
def del_space(text):
    new_text = ""
    for char in text:
        if char == " ":
            char = ""
        new_text += char
    return new_text
# del_space("Hola Mundo")


# DEFINIR FUNCION PARA REVERTIR PALABRA
def reverse_text(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text
# reverse_text("HoLaToDoS")


# DEFINIR PALABRA PALINDROM
def is_palondromo(text):
    text_del_space = del_space(text)
    text = reverse_text(text_del_space)
    return text.lower() == text_del_space.lower()


print(is_palondromo("Anna anna"))
print(is_palondromo("Compresión de las matemácticas"))
is_palondromo("Reconocer")
