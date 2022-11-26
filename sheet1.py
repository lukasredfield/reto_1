"""ESTA HOJA CREA EL ARCHIVO 'CSV' """

import pandas as pd
import csv


df = pd.read_csv('database.csv')


pivot = pd.pivot_table(df,index=['Theme','Country','Country'], values=['Country'], columns=['Author'],)

# Create DataFrame
data = pd.DataFrame(pivot)
 
# Write to CSV file
data.to_csv("Data_del_reto.csv")
 
# Print the output.
#print(data)

# with open('data.csv','w', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(Dic_Autores)

#df = pd.read_csv('Data_del_reto.csv')
df = pd.read_csv('Data_del_reto.csv')


