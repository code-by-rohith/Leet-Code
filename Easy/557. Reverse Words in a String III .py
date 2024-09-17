a="abcd efgh ijkl"
c=a.split()
temp=[]
for i in c:
    word=i[::-1]
    temp.append(word)
samp=" ".join(temp)
print(samp)

