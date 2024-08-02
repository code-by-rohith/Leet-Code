def can_partition(square, target):
    square_str = str(square)
    n = len(square_str)

    def dfs(index, current_sum):
        if index == n:
            return current_sum == target
        for end in range(index + 1, n + 1):
            num = int(square_str[index:end])
            if dfs(end, current_sum + num):
                return True
        return False

    return dfs(0, 0)


def num1(n):
    count = 0
    for i in range(1, n + 1):
        square = i * i
        if can_partition(square, i):
            count += square
    return count


# Example usage:
n = int(input("Enter a positive integer: "))
print(num1(n))
