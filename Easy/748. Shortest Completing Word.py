from collections import Counter

def main(licensePlate, words):
    letter_counts = Counter()
    for char in licensePlate:
        if char.isalpha():
            letter_counts[char.lower()] += 1

    def completes(word):
        word_counts = Counter(word)
        for char, count in letter_counts.items():
            if word_counts[char] < count:
                return False
        return True

    completing_words = []
    for word in words:
        if completes(word):
            completing_words.append(word)

    shortest_word = completing_words[0]
    for word in completing_words:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word

licensePlate1 = "1s3 PSt"
words1 = ["step", "steps", "stripe", "stepple"]
print(main(licensePlate1, words1))
