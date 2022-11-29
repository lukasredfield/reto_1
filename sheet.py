import gspread
import pandas as pd
import numpy as np


from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

credenciales = ServiceAccountCredentials.from_json_keyfile_name('python-sheets.json', scope)

cliente = gspread.authorize(credenciales)

sheet = cliente.create("Reto 1 - sheet")

sheet.share('lukasredfield@gmail.com', perm_type='user', role='writer')

sheet = cliente.open("Reto 1 - sheet").sheet1

database = pd.read_csv('Data TEST - Reto1.csv')

#columnas_base = database.groupby(['Country','Theme'],as_index=False).agg({'Author':'nunique','Sentiment':'nunique'})

data = pd.pivot_table(database, values=['Author', 'Sentiment'], index=['Country', 'Theme'], columns=['Author', 'Sentiment'], aggfunc={'Author':lambda x: "|".join(x), 'Sentiment':lambda x: "|".join(x), }).fillna('')

#print(pd.DataFrame(columnas_base))

pd.DataFrame(data).to_csv("Data_del_reto.csv")

df = pd.read_csv("Data_del_reto.csv")

df.fillna('',inplace=True)

if __name__=='__main__':
   sheet.update([df.columns.values.tolist()]+ df.values.tolist())