def lexicalOrder(n: int):
    numbers = [str(i) for i in range(1, n + 1)]
    numbers.sort()
    result = [int(num) for num in numbers]
    return result

print(lexicalOrder(13))
print(lexicalOrder(2))
