import numpy as np
import pandas as pd
from collections import Counter
import codecs

import matplotplib.pyplot as plt

path_romeo_and_juliet = 'Books/English/shakespeare/Romeo and Juliet.txt'

def read_file(path):
    with codecs.open(path,'r', encoding='utf8') as f:
        text = f.readlines()
    return ''.join(text)

text = read_file(path_romeo_and_juliet)
print(text)

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def word_count_distribution(text):
    (num_unique, counts) = word_stats(count_words_fast(text))
    r = (Counter(counts))
    return r


distribution = word_count_distribution(text)
print('-----------')
print("distribution")
print(distribution)
print('-----------')

def more_frequent(distribution):
    d = dict()
    for k, v in distribution.items():
        d[k] = k / v
    return d

print('-----------')
print("more frequent distribution")
print(more_frequent(distribution))
print('-----------')


def readHamlets():
    hamlets = pd.DataFrame(columns=("language", "distribution"))
    book_dir = "Books"
    title_num = 1
    book_titles = {'English': {'shakespeare': ("A+Midsummer Night's Dream",
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard III',
   'Romeo and Juliet',
   'The+Merchant+of+Venice')},
 'French': {'chevalier': ("L'enfer et le paradis de l'autre+monde",
   "L'i%CC%82le de sable",
   'La capitaine',
   'La fille des indiens rouges',
   'La fille du pirate',
   'Le chasseur noir',
   'Les derniers Iroquois')},
 'German': {'shakespeare': ('Der Kaufmann von Venedig',
   'Ein Sommernachtstraum',
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard III',
   'Romeo und Julia')},
 'Portuguese': {'shakespeare': ('Hamlet',)}}

    for language in book_titles:
        for author in book_titles[language]:
            for title in book_titles[language][author]:
                if title == "Hamlet":
                    inputfile = "Books/" + language + "/" + author + "/" + title + ".txt"
                    text = read_file(inputfile)
                    distribution = word_count_distribution(text)
                    hamlets.loc[title_num] = language, distribution
                    title_num += 1

def plot_word_frequency_distribution():
    hamlets = pd.DataFrame(columns=("language", "distribution"))
    colors = ["crimson", "forestgreen", "blueviolet"]
    handles, hamlet_languages = [], []
    for index in range(hamlets.shape[0]):
        language, distribution = hamlets.language[index + 1], hamlets.distribution[index + 1]
        dist = more_frequent(distribution)
        plot, = plt.loglog(sorted(list(dist.keys())), sorted(list(dist.values()),
                                                             reverse=True), color=colors[index], linewidth=2)
        handles.append(plot)
        hamlet_languages.append(language)
    plt.title("Word Frequencies in Hamlet Translations")
    xlim = [0, 2e3]
    xlabel = "Frequency of Word $W$"
    ylabel = "Fraction of Words\nWith Greater Frequency than $W$"
    plt.xlim(xlim);
    plt.xlabel(xlabel);
    plt.ylabel(ylabel)
    plt.legend(handles, hamlet_languages, loc="upper right", numpoints=1)
    # show your plot using `plt.show`!
    plt.show()

