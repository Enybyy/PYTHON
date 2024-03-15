from openai import OpenAI

# INGRESAR APIKEY
# INGRESAR API KEY
client = OpenAI(api_key=api_key)

# CONFIGURAR LA CLAVE DE LA API

# Mensaje de bienvenida
print("¡Bienvenido al Robot Erudito! Por favor, ingresa tu pregunta.")

# TEXTO PARA EL MODELO DE CHAT GPT-3
input_text = "Eres un robot erudito"

# Bucle de repetición
while True:
    # PARÁMETROS DE LA SOLICITUD A LA API DE OPENAI
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        # INPUT
        prompt=input("Ingresa tu pregunta: "),
        max_tokens=100  # NÜMERO MAX DE CHAR
    )

    # OBTENER LA RESPUESTA GPT-3
    output_text = response.choices[0].text.strip()

    # IMPRIMIR LA RESPUESTA GENERADA
    print("RESPUESTA DEL ROBOT ERUDITO:")
    print(output_text)

    # PREGUNTAR SI DESEA CONTINUAR
    continuar = input("¿Deseas hacer otra pregunta? (s/n): ")
    if continuar.lower() != "s":
        break  # BREAK LOOP
