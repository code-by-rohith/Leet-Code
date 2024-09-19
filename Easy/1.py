def main(n):
    def next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next(n)
    return n == 1
print(main(19))
print(main(2))

