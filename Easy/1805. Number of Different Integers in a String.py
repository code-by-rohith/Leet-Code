
word ="a1b01c001"
def num(word):
    a=[]
    b=""
    for letter in range(len(word)):
        if word[letter].isdigit():
            b+= word[letter]
        elif b:
            a.append(b)
            b=""
    if b:
        a.append(b)
    return len(set(int(nums) for nums in a))

print(num(word))