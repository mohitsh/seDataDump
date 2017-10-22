# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import fetchData as fd


def processor():
    posts = fd.table_reader('posts')
    badges = fd.table_reader('badges')

    # most used tags in posts, threshold is 25
    ptags = posts.Tags.value_counts()
    ptags = ptags[ptags>25]

    # most awarded badges, threshold is 1000
    bnames = badges.Name.value_counts()
    bnames = bnames[bnames>1000]

    #ptags.plot.pie(autopct="%.2f", fontsize=20, figsize=(12,12))
    #plt.tight_layout()
    
    print(bnames)
    bnames.plot.pie(autopct='%.2f', fontsize=20, figsize=(15, 15))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    processor()
