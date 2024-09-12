def print_x_number_pattern(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(num, end="")
            else:
                print(" ", end="")
        print()
        num += 1

size = 6
print_x_number_pattern(size)
