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


Autores = [
    ['Joseluna','Positive','Ecuador','PA'],['sixt93','Negative','Colombia','CA'],['alberto','Positive','Francia','OT'],['carlosz','Negative','USA','OT'],['jgbesq','Negative','UK','PA'],
    ['nuri90','Neutral','Spain','EV'],['santiago8','Neutral','Chile','KS'],['Joseluna','Positive','Peru','KS'],['alberto','Positive','Francia','OT'],['jgbesq','Negative','Panana','KS'],
    ['sixt93','Negative','Portugal','OT'],['santiago8','Neutral','Chile','KS'],['santiago8','Neutral','Bolivia','PA'],['nico23','Neutral','USA','PA'],['alberto','Positive','USA','KS'],
]

Dic_Autores = { '1':Autores[0],'2':Autores[1],'3':Autores[2],'4':Autores[3],'5':Autores[4],'6':Autores[5],'7':Autores[6],'8':Autores[7],'9':Autores[8],'10':Autores[9],'11':Autores[10],'12':Autores[11],'13':Autores[12],'14':Autores[13],'15':Autores[14],

}


df = pd.read_csv('Data_del_reto.csv')


sheet.update([df.columns.values.tolist()]+ df.values.tolist())




# tabla = sheet2.pivot_table(columns=[Author,Sentiment],)

#tabla = pd.pivot_table(df,index=['Author','Sentiment'], columns=['d'])


















