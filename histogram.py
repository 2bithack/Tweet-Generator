import sys

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


print(histogram())

def unique_words():
    return len(histogram())
print('Unique word count: ' + str(unique_words()))

def frequency():
    dictionary = histogram()
    inputWord = sys.argv[1]
    if inputWord in dictionary:
        return dictionary[inputWord]
print('That word is found ' + str(frequency()) + ' time(s).')
