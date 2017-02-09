import random
import sys

arr = sys.argv
def random_python_words():
    arr2 = []
    arr3 = arr[1:]
    print arr3
    for i in range(len(arr3)):
        rand_index = random.randint(0, len(arr3) - 1)
        arr2.append(arr3[rand_index])
        arr3.remove(arr3[rand_index])
    return arr2

if __name__ == '__main__':
    newSentence = random_python_words()
    print " ".join(newSentence)
