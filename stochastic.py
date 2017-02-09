import sys
import random

def open_file():
    with open("/Users/kn0t/Documents/MakeSchool/frontEndWebClass/front-end-React/webpack-starter/node_modules/stream-http/test/server/static/basic.txt", 'r') as f:
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
    arr = histogram().items()
    arr2 = []
    #the first for loop iterates through the entire array
    for i in range(len(arr)-1):
        #this for loop iterates the number of the token count from the dictionary(second tuple value)
        for j in range(arr[i][1]):
            #appending a new array with only the key of the tuple list
            arr2.append(arr[i][0])
    rand_index = random.randint(0, len(arr2) - 1)
    return arr2[rand_index]

print('Random word: ' + random_word())
