def main(word1, word2):
    temp = ''.join(word1)
    samp = ''.join(word2)
    return temp == samp

word1 =["a", "cb"]
word2 =["ab", "c"]
print(main(word1,word2))
