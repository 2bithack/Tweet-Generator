import random
import sys

def open_file():
    with open("/usr/share/dict/words", 'r') as f:
        corpus = f.read().splitlines()
        f.close()
        return corpus

def random_words():
    arr = open_file()
    arr2 = []
    arr3 = arr
    for i in range(int(sys.argv[1])):
        rand_index = random.randint(0, len(arr3) - 1)
        arr2.append(arr3[rand_index])
        arr3.remove(arr3[rand_index])
    return arr2

if __name__ == '__main__':
    newSentence = random_words()
    print " ".join(newSentence)
