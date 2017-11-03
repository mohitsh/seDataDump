# coding: utf-8

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd

def remove_angle_brackets(text_input):
    pat = r"[\w-]+"
    result_arr = re.findall(pat, text_input)
    result = ','.join(result_arr)
    return result

def processor(token):
    posts = fd.table_reader('posts')
    posts_tag_date = posts[['CreationDate', 'Tags']]
    posts_tag_date = posts_tag_date[posts_tag_date.Tags.notnull()]
    posts_tag_date['Tags'] = posts_tag_date['Tags'].apply(remove_angle_brackets)
    posts_tag_date_token = posts_tag_date[posts_tag_date['Tags'].str.contains(token)]


    start,end = posts_tag_date_token['CreationDate'].min(), posts_tag_date_token['CreationDate'].max()
    date_bins = pd.date_range(start, end, freq='M')

    storage = dict()
    for i in range(len(date_bins)-1):
        date_mask = (posts_tag_date_token['CreationDate'] > date_bins[i]) & (posts_tag_date_token['CreationDate'] <= date_bins[i+1])
        df = posts_tag_date_token.loc[date_mask]
        #key = '-'.join([str(x) for x in date_bins[i:i+1]])
        key = date_bins[i+1]
        val = len(df)
        if val == 0:
            print(date_bins[i], date_bins[i+1])
            pass
        else:
            storage[key] = val


    final_count = pd.DataFrame.from_dict([storage]).transpose()
    #final_count = final_count.reset_index()
    final_count.columns = [token]


    #final_count.plot(lw=0.5, style='b',figsize=(7,5), x='Time', y=token)
    #plt.show()
    return final_count


if __name__ == '__main__':
    tokens = ['r', 'python']
    tokens = ['data-mining', 'machine-learning']
    tokens = ['bigdata', 'hadoop']
    tokens = ['r', 'octave']
    tokens = ['clustering', 'predictive']
    for i, token in enumerate(tokens):
        df = processor(token)
        if i == 0:
            ax = df.plot()
        else:
            df.plot(ax = ax)

    plt.show()
