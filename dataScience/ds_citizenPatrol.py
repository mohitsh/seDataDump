
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd


def processor():
    location = fd.fetch_data('Citizen Patrol', 3)


    citizenPatrol_badge = {'India':3,
                           'United States':6,
                           'United Kingdom':4+3+3,
                           'France':3+3,
                           'Germany':7,
                           'Poland':3,
                           'Belgium':3}


    df_citizenPatrol_badge = pd.DataFrame.from_dict(citizenPatrol_badge, orient='index').reset_index()
    df_citizenPatrol_badge.columns = ['Country', 'Number of Citizen Patrol Badge Holders']



    sea.set(color_codes=True)
    sea.set_style('whitegrid')
    sea.stripplot(x='Country', y='Number of Citizen Patrol Badge Holders', data=df_citizenPatrol_badge, jitter=True, alpha=0.95, size=10)
    sea.despine(offset=20, trim=True)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    processor()
