
import sys
import random

class Markovtogram(dict):

    def word_list(self):
        with open("./basic.txt", 'r') as f:
            words = f.read().split()
            f.close()
        self.update(words)

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Markovtogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if word_list:
            self.update(word_list)

    def update(self, word_list):
        """Update this histogram with the items in the given iterable"""
        for index in range(0, len(word_list) - 1):
            if word_list[index] not in self:
                self[word_list[index]] = [word_list[index + 1]]
            else:
                self[word_list[index]].append(word_list[index + 1])
        return self


    def generate(self):
        rand_index = random.randint(1, (len(self.keys()) - 1))
        state = self.keys()[rand_index]
        sentence = []
        for i in range(20):
            next_word = random.choice(self[state])
            sentence.append(next_word)
            state = next_word
        return " ".join(sentence)


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if word not in self:
            return 0
        return self[word]

fish = Markovtogram(['one', 'fish', 'two', 'fish','red', 'fish', 'blue', 'fish'])
lamb = Markovtogram()
print(lamb.word_list())
