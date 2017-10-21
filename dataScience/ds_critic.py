
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd


def processor():
    location = fd.fetch_data('Critic', 2)

    critic_badge = {'India':6,
                'United States':3+3+2+2+2+2,
                'United Kingdom':4+2,
                'France':3,
                'Germany':4+2+2,
                'Singapore':2,
                'Spain':2,
                'Turkey':2,
                'Belgium':2,
                }


    df_critic_badge = pd.DataFrame.from_dict(critic_badge, orient='index').reset_index()
    df_critic_badge.columns = ['Country', 'Number of Critic Badge Holders']


    sea.set(color_codes=True)
    sea.set_style('whitegrid')
    sea.stripplot(x='Country', y='Number of Critic Badge Holders', data=df_critic_badge, jitter=True, alpha=0.95, size=10)
    sea.despine(offset=20, trim=True)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    processor()
