numers = (1, 2, 3)+(4, 5, 6)
print(numers)
punto = ([1, 2])
print(punto)
meNum = numers[:2]
print(meNum)

n1, n2, *n = numers
print(n1, n2, n)
for n in numers:
    print(n)


newN = list(numers)
newN[0] = "CERO"
print(newN)
