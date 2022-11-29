# # import gspread
# # import pandas as pd
# # import numpy as np


# # # from oauth2client.service_account import ServiceAccountCredentials

# # # scope = ['https://www.googleapis.com/auth/spreadsheets',
# # #         'https://www.googleapis.com/auth/drive']

# # # credenciales = ServiceAccountCredentials.from_json_keyfile_name('python-sheets.json', scope)

# # # cliente = gspread.authorize(credenciales)

# # # sheet = cliente.create("Reto 1 - sheet")

# # # sheet.share('lukasredfield0@gmail.com', perm_type='user', role='writer')

# # # sheet = cliente.open("Reto 1 - sheet").sheet1


# # datos = pd.read_csv('Data TEST - Reto1.csv')

# # df = pd.DataFrame(datos)

# # df2 = df.groupby(["Country", "Theme"], as_index=True)['Author'].apply(np.array).to_frame() #### Lo más lejos que llegué

# # df2.to_csv("Data_del_reto.csv")


# # #df2 = df.groupby(["Country"], as_index=True)['Author'].apply(np.array).to_frame()

# # #df3 = df.groupby(["Theme"], as_index=True)['Sentiment'].apply(np.array).to_frame()

# # #df4 = pd.concat([df2,df3])

# # print(df2)

# # #dff = pd.concat([df2, df3])

# # #print(dff)






# # df = pd.read_csv('Data TEST - Reto1.csv')

# # df.to_csv('Data TEST - Reto1.csv', sep=',', columns=True, index=True)

# # print(df.iloc[1, :2])

# #print(df)

# import pandas as pd
# import numpy as np

# database = pd.read_csv('Data TEST - Reto1.csv')

# database.to_csv("Data_del_reto.csv")

# #columnas_base = database.groupby(['Country','Theme'],as_index=False).agg({'Author':'nunique','Sentiment':'nunique'})

# columnas_base = pd.pivot_table(database, values=['Author', 'Sentiment'], index=['Country', 'Theme'], columns=['Author', 'Sentiment'], aggfunc={'Author':lambda x: "|".join(x), 'Sentiment':lambda x: "|".join(x), }).fillna('')

# print(pd.DataFrame(columnas_base))

# pd.DataFrame(columnas_base).to_csv("Data_del_reto.csv")



