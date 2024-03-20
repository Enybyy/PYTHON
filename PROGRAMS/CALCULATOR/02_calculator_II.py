# ----  CALCULATOR 2  ----

# MODULOS
from unidecode import unidecode

print("BIENVENIDOS A MI CALCULADORA")

operacion = ""
# LOOP - PARA REPETIR OPCIONES HASTA QUE SELECCIONE UNA ALTERNATIVA REQUERIDA
while True:

    n1 = int(input("Ingresa primer número: "))
    operacion = unidecode(input("Ingresa una operación: ").lower())
    # BREAK LOOP
    if operacion or n1 or n2 == "exit":
        print("Saliendo...")
        break
    n2 = int(input("Ingresa segundo número: "))
    x = n1

    if operacion == "suma":
        n1 += n2
        print(f"la suma del número {x} mas {n2} es igual a: ", n1)
    elif operacion == "resta":
        n1 -= n2
        print(f"la resta del número {x} menos {n2} es igual a: ", n1)
    elif operacion == "multiplicacion":
        n1 *= n2
        print(f"la multiplicación del número {x} por {n2} es igual a: ", n1)
    elif operacion == "division":
        n1 /= n2
        print(f"la suma del número {x} diividido en {n2} es igual a: ", n1)
    else:
        print(
            "Por favor ingrese una de estas 4 operacion que desee realizar alternativas:"
        )
        print("'Suma', 'Resta', 'Multiplicación', 'División'")
        print("O escriba 'exit' si desea salir de la calculadora")
