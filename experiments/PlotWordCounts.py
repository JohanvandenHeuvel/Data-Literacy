
import numpy as np
import tikzplotlib as tlp
import matplotlib.pyplot as plt
from matplotlib import ticker
import csv

import os

datapath = "../data/"
files = os.listdir(datapath)

print("-- generating plots for the following files --")
print(files)

for f in files:
    with open(os.path.join(datapath, f), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        results = [row for row in reader]

        term = f.split(".")[0]

        # first row contains words 
        words = results[0]
        words = words[:10]
        # second row contains counts
        counts = results[1]
        counts = counts[:10]

        fig, ax = plt.subplots(1, 1)
        idx = np.arange(len(counts))
        ax.bar(idx, height=counts[::-1], bottom=0)
        ax.set_xlabel("words")
        ax.set_ylabel("counts")
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.set_xticks(idx)
        ax.set_xticklabels(words[::-1], rotation=45)
        ax.set_title("Term: {}".format(term))

        # y-axis in inverted for some reason
        # plt.gca().invert_yaxis()
        # ax.legend()
        plt.tight_layout()

        plotpath = "../doc/{}.tex".format(term)
        print("-- saving to {} --".format(plotpath))

        tlp.save(
            plotpath, 
            axis_width = "\\figwidth",
            axis_height = "\\figheight",
            tex_relative_path_to_data = "./",
            strict = True,
        )