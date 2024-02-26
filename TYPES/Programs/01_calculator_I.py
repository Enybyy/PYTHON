import math

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))

suma = n1 + n2
rest = n1 - n2
mult = n1 * n2
divi = n1 / n2
pote = n1**n2
raiz = pow(n1, (1 / n2))

result = print(
    f"""
Resultado para la suma de {n1} y {n2} es {suma}
Resultado para la resta de {n1} y {n2} es {rest}
Resultado para la multiplicación de {n1} y {n2} es {mult}
Resultado para la división de {n1} y {n2} es {divi}
Resultado para la potecia de {n1} y {n2} es {pote}
Resultado para la raiz {n2} del número {n1} es {raiz}
"""
)
