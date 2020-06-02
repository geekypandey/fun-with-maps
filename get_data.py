import sqlite3

import requests
import pandas as pd

url = 'https://www.sport-histoire.fr/en/Geography/Countries_by_alphabetical_order.php'

def get_df(url):
    res = requests.get(url)
    df = pd.read_html(res.text, header=0)[0]
    return df

if __name__ == '__main__':
    df = get_df(url)
    df.to_csv('data.csv', index=False)
