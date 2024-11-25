s = "is2 sentence4 This1 a3"
data = s.split()
temp = [""]*len(data)
for i in data:
    a=""
    for j in i:
        if not j.isdigit():
            a+=j
        if j.isdigit():
            temp[int(j)-1] = a
print(" ".join(temp))


