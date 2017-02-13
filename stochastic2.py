import sys
import random

def open_file():
    with open("./basic.txt", 'r') as f:
        words = f.read().split()
        f.close()
    return words

def histogram():
    #could use re instead of strip
    unwanted_chars = """.,-_?""'<>}{)("""
    dictionary = {}
    for raw_word in open_file():
        word = raw_word.strip(unwanted_chars).lower()
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1
    return dictionary

def random_word():
    rand_index = random.randint(1, sum(histogram().values()))
    count = 0
    for key in histogram():
        count += histogram()[key]
        if count >= rand_index:
            return key
print('Random word: ' + random_word())
