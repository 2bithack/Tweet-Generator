def open_file():
    with open("./basic.txt", 'r') as f:
        words = f.read().split()
        f.close()
    return words

def clean_file():
    #could use re instead of strip
    unwanted_chars = """.,-_?""'<>}{)("""
    clean_list = []
    for raw_word in open_file():
        word = raw_word.strip(unwanted_chars).lower()
        clean_list.append(word)
    return clean_list

# print(clean_file())
