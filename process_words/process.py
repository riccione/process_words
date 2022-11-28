'''
Goal:
Get new (unknown) words from the text or link

Process txt file to get a word list from it
If the word is in known list => exclude it from the final list
Create a final result list with new words
'''
import re


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        data = clean(data)
        words = set(data.split(' '))
    return list(words)

def clean(x):
    x = re.sub('[\'\"”\.,;:!?+\-=!@#$%^&*—/]', '', x)
    x = re.sub('[\(\)]', '', x)
    x = re.sub('\d', '', x)
    x = x.replace('\n', '')
    return x.lower()

def is_known(x):
    xz = []
    with open('./known.txt', 'r') as f:
        data = f.read()
        for w in x:
            if w not in data and w != '':
                xz.append(w)
    return xz


def save_file(x):
    with open('./final.txt', 'w') as f:
        for v in x:
            f.write(f"{v}\n")


data = read_file('./sample.txt')
data = is_known(data)
data = sorted(data)
save_file(data)