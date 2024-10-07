def find_key(num1, num2, num3):
    str1 = str(num1).zfill(4)
    str2 = str(num2).zfill(4)
    str3 = str(num3).zfill(4)
    key_digits = []
    
    for i in range(4):
        min_digit = min(str1[i], str2[i], str3[i])
        key_digits.append(min_digit)
    
    key = ''.join(key_digits)
    return int(key)

result = find_key(1, 10, 1000)
print(result) 
