s = "RLRRLLRLRL"
temp=0
samp=0
for i in s:
    if i =='L':
        temp +=1
    elif i =="R":
         temp -=1
    if temp==0:
        samp+=1

print(samp)
