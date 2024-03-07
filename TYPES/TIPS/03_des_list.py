numbers = [1, 2, 3, 4, 5]

# bad
# prim0 = numbers[0]
# prim1 = numbers[1]
# prim2 = numbers[2]
# prim3 = numbers[3]
# prim4 = numbers[4]

n1, n2, n3, n4, n5 = numbers
print(n1, n2, n3, n4, n5)

n1, *n, n3, n4 = numbers
print(n1, n3, n4)
