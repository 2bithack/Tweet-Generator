import sys
import random
import stochastic2

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! Your random word from the great poem "Mary had a little lamb" is: ' + str(stochastic2.random_word())
