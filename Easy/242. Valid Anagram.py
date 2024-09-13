def main(s,t):
        if len(s)==len(t):
            temp = sorted(s)
            samp = sorted(t)
            count = 0
            for i in range(len(temp)):
                if temp[i]==samp[i]:
                    count +=1
            if count== len(samp) and len(temp):
                return True
            else:
                return False
        return False

s = "anagramsa"
t = "nagaram"
print(main(s,t))