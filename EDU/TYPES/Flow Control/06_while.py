# LOOP INFINITE - WHILE & IF

# num = 0

# while num < 100:
#     print(num)
#     num += 5


# ¡"AND" o "OR"?
# CUANDO EL COMANDO SEA DIFERENTE A "salir" Y DIFERENTE A "salir" SIGUE EJECUTANDO EL SCRIPT -
# ESTO QUIERE DECIR QUE SI "command" NO ES DIFERENTE ALGUNA DE LAS DOS OPCIONES POR LO TANTO SERÁ IGUAL A ALGUNA DE ELLAS, EL SCRIPT SE DETENDRÁ.
# CASO CONTRARIO: CUANDO EL COMANDO SEA DIFERENTE A "salir" o DIFERENTE A "salir" SIGUE EJECUTANDO EL SCRIPT -
# ESTO QUIERE DECIR QUE SI "command" ES DIFENTE ALGUNA DE LAS DOS OPCIONES EL SCRIPT SEGUIRÁ EJECUTANDOSE, PERO SI ES IGUAL A LAS DOS SE DETENRÁ.
command = ""
# while command.lower() != "salir":
while command != "salir" and command.lower() != "salir":
    command = input("$ ")
    print(command)
    if command == "infinite":
        # BUCLE INFINITO
        while True:
            command = input('ESCRIBA "SALIR" PARA ROMPERE EL BUCLE: ')
            if command == "SALIR":
                break
