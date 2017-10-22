
# coding: utf-8

import pandas as pd
import numpy as np
import pymysql as mysql
import matplotlib.pyplot as plt
import seaborn as sea
import cred


def get_conn():
    host = cred.host_name
    user = cred.user_name
    passwd = cred.passwd
    db = cred.db_name

    conn = mysql.connect(host=host, user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    return conn


def db_processing(token):
    conn = get_conn()
    tags_query = "SELECT * FROM tags"
    tags = pd.read_sql(tags_query, conn)

    posts_query = "SELECT Id, Body,OwnerUserId, PostTypeId, Score,ViewCount, Title,Tags, AnswerCount, CommentCount FROM posts"
    posts = pd.read_sql(posts_query, con=conn)

    badges_query = "SELECT * FROM badges"
    badges = pd.read_sql(badges_query, con=conn)



    users_query = "SELECT Id, DisplayName, Reputation,CreationDate, Location, AboutMe, Views, UpVotes, DownVotes, AccountId FROM users"
    users = pd.read_sql(users_query, con=conn)



    badges_sub = badges.loc[badges['Name'] == token]
    complete_info = pd.merge(badges_sub, users, left_on= 'UserId', right_on='Id')
    return complete_info


def fetch_data(token, e):
    complete_info = db_processing(token)
    location = complete_info.Location.value_counts()
    location = location[location>=e]
    return location


def draw_plot():
    location = fetch_data('Citizen Patrol', 3)
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
    draw_plot()
