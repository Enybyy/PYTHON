import requests
import json

"""
url = "https://rickandmortyapi.com/api/character/1"
r = requests.get(url)
# response = r.text
j = r.json()
# print(j.keys())
estado = j['status']
print("El estado del personaje es: ", estado)


for i in range(1, 11):
    url = f"https://rickandmortyapi.com/api/character/{i}"
    r = requests.get(url)
    j = r.json()
    nombre = j['name']
    estado = j['status']
    print(f"{i}: El personaje {nombre} tiene un estado de: {estado}")
"""

# LLAMAR URL
url = "https://rickandmortyapi.com/api/episode/1"
r = requests.get(url)
j = r.json()

personajes = j['characters']
list_char_episode_1 = list()
list_especie_humano = list()
list_especie_no_humano = list()

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    nombre = js['name']
    list_char_episode_1.append(nombre)
    if js['species'] == 'Human':
        list_especie_humano.append(nombre)
    else:
        list_especie_no_humano.append(nombre)

print(f"Nombre de los personajes del episodio 1: {
      list_char_episode_1}\nDe los cuales existen lo personajes 'humanos' y los 'no humanos'")
print("Nombre de los personajes humanos: ", list_especie_humano)
print("Nombre de los personajes no humanos: ", list_especie_no_humano)
