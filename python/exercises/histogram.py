import sys



def open_file():
    with open("/users/kn0t/Documents/gameDescriptions.docx", 'r') as f:
        corpus = f.read().splitlines()
    f.close()
print f

open_file()
