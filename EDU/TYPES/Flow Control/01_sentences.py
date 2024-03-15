# IF, Elif & Else

edad = int(input("Ingrese su edad por favor: "))

print(
    """Por favor ingrese su edad para poder saber si califica a 
nuestras promociones y si es apto para poder ver esta pelicula"""
)
if edad >= 60:
    print("Usted puede ver la pelcula y califica para un descuento del 40%")
elif edad >= 45:
    print("Usted puede ver la pelcula y califica para un descuento del 20%")
elif edad >= 18:
    print(
        "Usted puede ver la pelcula, peor lamentablemente no califica para ninguna de nuestras promociones :("
    )
else:
    print("Usted no califica para poder ver esta pelicula.")
