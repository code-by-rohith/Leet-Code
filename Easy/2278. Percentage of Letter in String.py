
def main(s,letter):
    count = {}
    for i in s:
        if i in count and i == letter:
            count[i] +=1
        else:
            count[i]=1
    a = count.get(letter,0)
    temp = a/len(s)
    fin = temp*100
    print(int(fin))


s = "foobar"
letter = "o"

main(s,letter)