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
        


    #date_bins = [pd.Timestamp('2014-05-13 23:58:30'), pd.Timestamp('2014-12-31 23:59:59'), pd.Timestamp('2015-01-01 00:00:00'),pd.Timestamp('2015-06-30 23:59:59'), pd.Timestamp('2015-07-01 00:00:00'),pd.Timestamp('2015-12-31 23:59:59'), pd.Timestamp('2016-01-01 00:00:00'),pd.Timestamp('2016-06-30 23:59:59'), pd.Timestamp('2016-07-01 00:00:00'),pd.Timestamp('2016-12-31 23:59:59')]


    #date_mask1 = (posts_tag_date_token['CreationDate'] > date_bins[0]) & (posts_tag_date_token['CreationDate'] <= date_bins[1])
    #df1 = posts_tag_date_token.loc[date_mask1]

    #date_mask2 = (posts_tag_date_token['CreationDate'] > date_bins[2]) & (posts_tag_date_token['CreationDate'] <= date_bins[3])
    #df2 = posts_tag_date_token.loc[date_mask2]

    #date_mask3 = (posts_tag_date_token['CreationDate'] > date_bins[4]) & (posts_tag_date_token['CreationDate'] <= date_bins[5])
    #df3 = posts_tag_date_token.loc[date_mask3]

    #date_mask4 = (posts_tag_date_token['CreationDate'] > date_bins[6]) & (posts_tag_date_token['CreationDate'] <= date_bins[7])
    #df4 = posts_tag_date_token.loc[date_mask4]

    #date_mask5 = (posts_tag_date_token['CreationDate'] > date_bins[8]) & (posts_tag_date_token['CreationDate'] <= date_bins[9])
    #df5 = posts_tag_date_token.loc[date_mask5]


    #storage = {'2014-05-13 - 2014-12-31':len(df1), '2015-01-01 - 2015-06-30':len(df2), '2015-07-01 - 2015-12-31':len(df3), '2016-01-01 - 2016-06-30':len(df4), '2016-07-01 - 2016-12-31':len(df5)}

    final_count = pd.DataFrame.from_dict([storage]).transpose()
    final_count = final_count.reset_index()
    final_count.columns = ['time_frame', 'val_count']


    #sea.set(color_codes=True)
    #sea.set_style('whitegrid')
    #sea.stripplot(x='time frame', y='count', data=final_count, jitter=True, alpha=0.95, size=13, palette="Set1")
    #sea.tsplot(data=final_count, value="val_count", time="time_frame")
    #sea.despine(offset=20, trim=True)
    #plt.xticks(rotation=45, fontsize=10)
    #plt.tight_layout()
    #plt.show()

    print(len(final_count.time_frame))
    print(len(final_count.val_count))


    #final_count[['val_count']].plot()
    final_count.plot(lw=0.5, style='b',figsize=(7,5), x='time_frame', y='val_count')
    #plt.plot(final_count.time_frame, final_count.val_count)
    plt.show()

if __name__ == '__main__':
    token = 'classification'
    processor(token)
