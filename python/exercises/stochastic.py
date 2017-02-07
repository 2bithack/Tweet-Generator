import sys
import random

def open_file():
    with open("/Users/kn0t/Documents/MakeSchool/frontEndWebClass/front-end-React/webpack-starter/node_modules/stream-http/test/server/static/basic.txt", 'r') as f:
        words = f.read().split()
        f.close()
    return words

def histogram():
    unwanted_chars = """.,-_?""'<>}{)("""
    dictionary = {}
    for raw_word in open_file():
        word = raw_word.strip(unwanted_chars).lower()
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1
    return dictionary

def random_word():
    arr = histogram().items()
    totalTokens = sum(histogram().values())
    print('Total words:' + str(totalTokens))
    arr2 = []
    print(arr)
    for i in range(totalTokens):
        rand_index = random.randint(0, totalTokens - 1)
        arr2.append(arr[rand_index])
        arr.remove(arr[rand_index])
    return arr2[rand_index]
print('Random word: ' + str(random_word()))
