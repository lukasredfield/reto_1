# """ESTA HOJA CREA EL ARCHIVO 'CSV' """

# import pandas as pd
# import csv


# df = pd.read_csv('Data TEST - Reto1.csv')



# pivot = pd.pivot_table(df,index = ["Country"], columns = ["Theme"], values = ["Author"])


# # Create DataFrame
# data = pd.DataFrame(pivot)
 
# # Write to CSV file
# data.to_csv("Data_del_reto.csv")
 
# Print the output.
#print(data)

# with open('data.csv','w', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(Dic_Autores)

#df = pd.read_csv('Data_del_reto.csv')
#df = pd.read_csv('Data_del_reto.csv')



# import gspread
# import pandas as pd
# import numpy as np


# from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://www.googleapis.com/auth/spreadsheets',
#         'https://www.googleapis.com/auth/drive']

# credenciales = ServiceAccountCredentials.from_json_keyfile_name('python-sheets.json', scope)

# cliente = gspread.authorize(credenciales)

# sheet = cliente.create("Reto 1 - sheet")

# sheet.share('lukasredfield0@gmail.com', perm_type='user', role='writer')

# sheet = cliente.open("Reto 1 - sheet").sheet1

# df = pd.read_csv('Data TEST - Reto1.csv')

# #df2.fillna('',inplace=True)

# data = pd.DataFrame(df)

# df = pd.DataFrame(data)

# df2 = df.groupby(["Country", "Theme"], as_index=True)['Author'].apply(np.array).to_frame() #### Lo más lejos que llegué

# df2.to_csv("Data_del_reto.csv")
 
# data.to_csv("Data_del_reto.csv")

# #print(data)

# df3 = pd.read_csv("Data_del_reto.csv")


# #pivot = pd.pivot_table(df,index=['Author','Sentiment'], columns=['d'])
# #sheet.update([df.columns.values.tolist()]+ df.values.tolist())

# #################################
# # print(df.info)          ###devuelve toda la lista
# # print(df.columns)       ###devuelve las columnas, quizas hay que rescatarlas de aca en 2 listas distintas y que se pasen esas listas al pivot_table

# ### author y sentiment se acomodan bien pero si le pasas en las columns country y theme te lo pone 1 encima del otro, y se tendrian que ver de costado
# #pivot = pd.pivot_table(df, index=['Author','Sentiment'], values=['Country','Theme'], columns='')    ### en columns habria que ver la forma de agregar country y theme como valores de una columna vacia
# #print('Columns(Author + Sentiment) to Index and avg by values \n%s' % pivot[:5])

# #pivot = pd.pivot_table(df,index = ["Country","Theme"], columns = ["Author", "Sentiment"])

# #print(pivot)

# if __name__=='__main__':
#     sheet.update([df3.columns.values.tolist()]+ df3.values.tolist())