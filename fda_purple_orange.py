import os

import pandas as pd
import sqlite3
import sqlalchemy

df = pd.read_csv('C:\\Users\\FM Inventario\\Documents\\fda_purple_orange_books.csv')
print(df)

query = '''
CREATE TABLE IF NOT EXISTS applicants (
    applicant STRING PRIMARY KEY,
);
'''

query2 = '''
CREATE TABLE IF NOT EXISTS drugs (
    bla_nda_number INT PRIMARY KEY,
    is_biologic BOOLEAN,
    proprietary_name STRING,
    proper_name STRING,
    
);
'''

df.tosql('aff',engine,index=False, if_exists='append')