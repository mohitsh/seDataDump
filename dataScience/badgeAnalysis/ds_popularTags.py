# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import fetchData as fd


def processor():
    posts = fd.table_reader('posts')
    ptags = posts.Tags.value_counts()
    ptags = ptags[ptags>25]
    print(ptags)
    ptags.plot.pie(autopct="%.2f", fontsize=20, figsize=(12,12))
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    processor()
