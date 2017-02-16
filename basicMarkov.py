import histograms
import stochastic2
import sys
import random

class Markovtogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Markovtogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if word_list:
            self.update(word_list)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for word in word_list:
            if word in self:
                self[word] += 1
            else:
                self[word] = 1
                self.types += 1
            self.tokens += 1


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if word not in self:
            return 0
        return self[word]
