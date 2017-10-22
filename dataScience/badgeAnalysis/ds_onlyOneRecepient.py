# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import fetchData as fd

def processor():
    oneRecepientBadge = ['Inquisitive', 'Stellar Question', 'Synonymizer']
    storage = {}
    for badge in oneRecepientBadge:
        df = fd.db_processing(badge)
        key = df.Name.to_string(index=False)
        user_name = df.DisplayName.to_string(index=False)
        location  = df.Location.to_string(index=False)
        reputation = df.Reputation.to_string(index=False)
        storage[key] = [user_name, location, reputation]

    return storage 

if __name__ == '__main__':
    result = processor()
