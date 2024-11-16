
def main(s):
        n=len(s)
        r=0
        for i in range(n+1):
            for j in range(i+1,n+1):
                a=(s[i:j])
                c=0
                for k in a:
                    if(a.count(k)>2):
                        c+=1
                        break
                if(c==0):
                    r=max(r,len(a))
        return(r)

s = "bcbbbcba"
print(main(s))