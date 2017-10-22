
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd


def processor():
    location = fd.fetch_data('Revival', 3)

    revival_badge = {'India':7+3,
                    'United States':8+4,
                    'United Kingdom':5,
                    'Romania':3,
                    'Germany':7+3,
                    'Series of tubes':3,
                    'Between 0 and 1':3,
                    }


    df_revival_badge = pd.DataFrame.from_dict(revival_badge, orient='index').reset_index()
    df_revival_badge.columns = ['Country', 'Number of Revial Badge Holders']


    sea.set(color_codes=True)
    sea.set_style('whitegrid')
    sea.stripplot(x='Country', y='Number of Revial Badge Holders', data=df_revival_badge, jitter=True, alpha=0.95, size=10)
    sea.despine(offset=20, trim=True)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    processor()
