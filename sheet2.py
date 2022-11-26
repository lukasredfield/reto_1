""" ESTA HOJA TOMA EL ARCHIVO CSV CREADO DEL SHEET1 Y LO CREA EN GOOGLE DRIVE CON EL NOMBRE DE "Reto 1 - sheet" """

import gspread
import pandas as pd


from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

credenciales = ServiceAccountCredentials.from_json_keyfile_name('python-sheets-369803-b64a0d78b3bf.json', scope)

cliente = gspread.authorize(credenciales)

sheet = cliente.create("Reto 1 - sheet")

sheet.share('lukasredfield@gmail.com', perm_type='user', role='writer')

sheet = cliente.open("Reto 1 - sheet").sheet1


df = pd.read_csv('Data_del_reto.csv')

df.fillna('',inplace=True)

sheet.update([df.columns.values.tolist()]+ df.values.tolist())

# sheet.update([df.columns.values.tolist()]+ df.values.tolist())

# pivot = pd.pivot_table(df,index=['Author','Sentiment'], columns=['d'])




















