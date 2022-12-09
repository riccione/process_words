"""
Goal:
Get new (unknown) words from the text or link

Process txt file to get a word list from it
If the word is in known list => exclude it from the final list
Create a final result list with new words

TODO: measure performance using profiler
TODO: argparse (filename for read)
TODO: make a class
TODO: make a library

"""
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import argparse
from pathlib import Path

def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        tokenizer = RegexpTokenizer(r"\w+")
        words = tokenizer.tokenize(data)
    return words


def get_stem(xz):
    xy = []
    wnl = WordNetLemmatizer()
    for x in xz:
        if len(x) > 1 and not x.isnumeric():
            xy.append(wnl.lemmatize(x.lower()))
    return xy


def is_known(xz):
    xy = []
    with open("./known.txt", "r") as f:
        known = f.read()
        for x in xz:
            if x not in known:
                xy.append(x)
    return xy


def count_frequency(xz, xz_set):
    xy = []
    for x in xz_set:
        if x != "":
            xy.append((x, xz.count(x)))
    return xy


def save_file(x):
    with open("./final.txt", "w") as f:
        last = 0
        for i, v in enumerate(x):
            f.write(f"{v[0]}, {v[1]}\n")
            last = i
    print(f"Unknown words: {last}")


def sort_by_frequency(xz):
    return sorted(xz, key=lambda x: x[1], reverse=True)

def is_file_exist(x):
    if x is not None:
        x = Path(x)
        if x.is_file():
            return True
    return False

def combine(x):
    data = read_file(x)
    data = get_stem(data)
    data = is_known(data)
    data = count_frequency(data, set(data))
    data = sort_by_frequency(data)
    save_file(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="path to text file", type=str)
    args = parser.parse_args()
    if is_file_exist(args.filename):
        combine(args.filename)
    else:
        print("File not found. Please provide a valid path to filename")

if __name__ == "__main__":
    main()