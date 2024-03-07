strings = ["hello", "idk", "idu", "from", "idk", "comida", "idk"]

# ADD
strings.insert(1, "world")
strings.append("no sé")

# DEL
# REMOVER
strings.remove("idk")
# ELIMINAR ULTIMO/ indx
strings.pop()
strings.pop(3)
del strings[4]
print(strings)
# ELIMINAR LIST
strings.clear()
print(strings)
