#!usr/bin/env python

def word_count(filename):
    wordcount = {}
    with open(filename) as f:
        for word in f.read().split():
            if wordcount.has_key(word):
                wordcount[word] += 1
            else:
                wordcount[word] = 1
    print(wordcount)

if __name__ == "__main__":
    filename = "wordcount.txt"
    word_count(filename)