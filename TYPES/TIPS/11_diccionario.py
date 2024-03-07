punto = {"x": 300, "y": 600}
print(punto)
print(punto["x"])
print(punto["y"])
punto["z"] = 100
print(punto)

if "w" in punto:
    print(punto, punto["w"])

# METODO GET:
print(punto.get("x"))
print(punto.get("w", 400))
del punto["x"]
del (punto["y"])
print(punto)
punto["x"] = 300
punto["y"] = 300

for val in punto:
    print(val, punto[val])

for val in punto.items():
    print(val)

for llave, val in punto.items():
    print(llave, val)

# R
users = [
    {"id": 1, "name": "Rogelio"},
    {"id": 2, "name": "Rodolfo"},
    {"id": 3, "name": "Rodrigez"},
    {"id": 4, "name": "Rojo"},
    {"id": 5, "name": "Ricardo"},
]

for user in users:
    print(user["name"])
