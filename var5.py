def print_sequence(rows):
    for i in range(rows):
        # Print leading spaces
        for _ in range(rows - i - 1):
            print("_", end=" ")
        # Print numbers in ascending order
        for j in range(rows - i, rows + 1):
            print(j, end=" ")
        print()

rows = 5
print_sequence(rows)


