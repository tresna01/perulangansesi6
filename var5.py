a = 5
b = 5

for i in range(5, 0, -1):
    for f in range(1, 5 + 1):
        if f < i:
            print("-", end=" ")
        else:
            print(f, end=" ")
    print()