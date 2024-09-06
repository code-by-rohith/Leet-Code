def main(n):
    arr=[]
    stack=[]

    def back_track(openN,closeN):
        if openN==closeN==n:
            stack.append("".join(arr))
            return
        if openN<n :
            arr.append("(")
            back_track(openN+1,closeN)
            arr.pop()
        if closeN<openN :
            arr.append(")")
            back_track(openN,closeN+1)
            arr.pop()
    back_track(0,0)
    return stack

print(main(3))