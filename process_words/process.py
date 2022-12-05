'''
Goal:
Get new (unknown) words from the text or link

Process txt file to get a word list from it
If the word is in known list => exclude it from the final list
Create a final result list with new words

TODO: measure performance using profiler
TODO: argparse (filename for read)
TODO: make a class
TODO: make a library

'''
import re


'''
read file
'''


def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        words = make_word_list(lines)
    return words


def make_word_list(xz):
    words = []
    with open('./known.txt', 'r') as f:
        known = f.read()
        for x in xz:
            xy = x.split()
            for v in xy:
                v = clean(v)
                if v not in known and v[:-1] not in known and v != '':
                    words.append(v)
    return words


def count_frequency(xz, xz_set):
    xy = []
    for x in xz_set:
        if x != '':
            xy.append((x, xz.count(x)))
    return xy


'''
remove punctuation, new lines
'''


def clean(x):
    return re.sub(r'[^a-zA-Z\']', '', x).lower()


'''
save all unknown words to final.txt
'''


def save_file(x):
    with open('./final.txt', 'w') as f:
        last = 0
        for i, v in enumerate(x):
            f.write(f"{v[0]}, {v[1]}\n")
            last = i
    print(f"Unknown words: {last}")


def sort_by_frequency(xz):
    return sorted(xz, key=lambda x: x[1], reverse=True)


data = read_file('./sample.txt')
data = count_frequency(data, set(data))
data = sort_by_frequency(data)
save_file(data)
