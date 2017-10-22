# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd

def processor():
    location = fd.fetch_data('Scholar', 3)

    scholar_badge = {'India':16+4,
                    'United States':9+4+3+3+3,
                    'United Kingdom':7+3,
                    'Israel':6,
                    'Australia':5,
                    'France':5,
                    'Germany':4+3+3,
                    'Russia':4+3,
                    'Iran':3+3,
                    'China':3,
                    'Netherlands':3,
                    'Singapore':3,
                    'HongKong':3,
                    }


    df_scholar_badge = pd.DataFrame.from_dict(scholar_badge, orient='index').reset_index()
    df_scholar_badge.columns = ['Country', 'Number of Scholar Badge Holders']


    sea.set(color_codes=True)
    sea.set_style('whitegrid')
    sea.stripplot(x='Country', y='Number of Scholar Badge Holders', data=df_scholar_badge, jitter=True, alpha=0.95, size=15)
    sea.despine(offset=20, trim=True)
    plt.xticks(rotation=90, fontsize=15)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    processor()
