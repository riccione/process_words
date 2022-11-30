'''
Goal:
Get new (unknown) words from the text or link

Process txt file to get a word list from it
If the word is in known list => exclude it from the final list
Create a final result list with new words

TODO: measure performance
TODO: argparse (filename for read)
TODO: make a class
TODO: make a library

'''
import re
# import nltk
# nltk.download('punkt')

'''
read file
'''


def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        words = make_word_list(lines)
        #data = f.read()
        #data = clean(data)
        # words = set(data.split())
        # words = set(nltk.word_tokenize(data))
    return list(words)


def make_word_list(xz):
    words = []
    for x in xz:
        xy = x.split()
        for v in xy:
            words.append(clean(v))
    return set(words)

'''
remove punctuation, new lines
'''


def clean(x):
    x = re.sub(r'[\'\"\”…\.,;:!?+\-=!“@#$%^&*—/]', '', x)
    x = re.sub(r'[\(\)]', '', x)
    x = re.sub(r'\d', '', x)
    x = x.replace('\n', '')
    return x.lower()


'''
known.txt file contains the list of known words
'''


def is_known(x):
    xz = []
    with open('./known.txt', 'r') as f:
        data = f.read()
        for w in x:
            if w not in data and w != '':
                xz.append(w)
    return xz


'''
save all unknown words to final.txt
'''


def save_file(x):
    with open('./final.txt', 'w') as f:
        for v in x:
            f.write(f"{v}\n")


data = read_file('./sample.txt')
data = is_known(data)
data = sorted(data)
save_file(data)
