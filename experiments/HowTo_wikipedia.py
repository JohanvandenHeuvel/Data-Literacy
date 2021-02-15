"""
Give as argument a string term, returns word count as .csv
e.g. python HowTo_wikipedia.py "Test"
"""

import re
import wikipedia
import numpy as np
import pandas as pd
import sys
import csv

def get_pages(args):
    # get wikipedia page for every term in args
    return [wikipedia.page(arg) for arg in args]

def word_count(page):
    assert page is not None
    # return sorted word count of page
    unique, count = np.unique(page.content.split(" "), return_counts=True)
    count_sort_ind = np.argsort(-count)
    return unique[count_sort_ind], count[count_sort_ind]

if __name__=="__main__":
    # containing search terms
    args = sys.argv[1:]
    pages = get_pages(args)
    # word_counts = [list(zip(*word_count(page))) for page in pages]
    word_counts = [word_count(page) for page in pages]

    for i, arg in enumerate(args):
        path = "../data/{}.csv".format(arg)
        print("-- writing {} to {} --".format(arg, path))
        with open(path, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(word_counts[i])



    
