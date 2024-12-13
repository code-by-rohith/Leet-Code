def main(s,indices):
    a = [""] * len(s)
    for i in range(len(indices)):
        a[indices[i]] = s[i]
    return "".join(a)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(main(s,indices))