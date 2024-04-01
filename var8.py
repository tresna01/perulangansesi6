a = 1
b = 1
c = 2

for i in range(7):
    print(" * " * a)
    c = b
    b =a + b
    a = c
print()