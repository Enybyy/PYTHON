# def saludar():
#     saludo = "Holas a todos"
#     print(saludo)


# def preguntar():
#     saludo = "¿Cómo estás?"
#     print(saludo)


# saludar()
# preguntar()


# SCOPE
saludo = "Hola mundo"


def saludar():
    global saludo
    saludo = "Hola a todos"
    # print(saludo)


def preguntar():
    saludo = "¿Cómo estás?"
    print(saludo)


print(saludo)
saludar()
print(saludo)
