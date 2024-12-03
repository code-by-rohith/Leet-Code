
def main(number, digit):
    max_result = ""
    for i in range(len(number)):
        if number[i] == digit:
            new_number = number[:i] + number[i+1:]
            if new_number > max_result:
                max_result = new_number
    return max_result

print(main())