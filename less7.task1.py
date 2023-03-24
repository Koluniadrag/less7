def count_words(sentence):
    words = sentence.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
sentence = 'TWalk fast, but think clearly'
word_counts = count_words(sentence)
print(word_counts)





