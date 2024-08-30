def fun():
    m=[]
    row = int(input("Enter the row :"))
    col = int(input("Enter the col :"))
    for i in range(row):
        a=[]
        for j in range(col):
            n=int(input())
            a.append(n)
        m.append(a)
    print(m)
fun()