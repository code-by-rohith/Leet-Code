
def main(a,b):
        count = 0
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count

print(main(12,6))
