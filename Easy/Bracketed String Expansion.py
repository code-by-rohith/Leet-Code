word = "3[a]4[bc]"
emptyword = ""
num = ""
substring=""
for letter in word:
    if letter.isdigit():
        num += letter
    elif letter == '[':
        continue
    elif letter == ']':
        emptyword += substring * int(num)
        num = ""
        substring=""
    else:
        substring += letter

print(emptyword)
