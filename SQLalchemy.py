# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:20:19 2023

@author: FM Inventario
"""

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///C:\\Users\\FM Inventario\\PycharmProjects\\Big_Data\\live_test_sqlite.db')

df = pd.read_csv('C:\\Users\\FM Inventario\\Documents\\fda_purple_orange_books.csv')

with engine.connect() as conn:
    df.to_sql('fda', conn, index=False, if_exists='append')

df2 = pd.read_sql('SELECT * FROM aff', engine)

print(df2)