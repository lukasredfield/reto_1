import gspread
import pandas as pd
import numpy as np


from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

credenciales = ServiceAccountCredentials.from_json_keyfile_name('python-sheets.json', scope)

cliente = gspread.authorize(credenciales)

sheet = cliente.create("Reto 1 - sheet")

sheet.share('lukasredfield0@gmail.com', perm_type='user', role='writer')

sheet = cliente.open("Reto 1 - sheet").sheet1

df = pd.read_csv('database1.csv')

df.fillna('',inplace=True)

# pivot = pd.pivot_table(df,index=['Author','Sentiment'], columns=['d'])

sheet.update([df.columns.values.tolist()]+ df.values.tolist())






















