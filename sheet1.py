"""ESTA HOJA CREA EL ARCHIVO 'CSV' """

import pandas as pd
import csv


Autores = [
    ['Joseluna','Positive','Ecuador','PA'],['sixt93','Negative','Colombia','CA'],['alberto','Positive','Francia','OT'],['carlosz','Negative','USA','OT'],['jgbesq','Negative','UK','PA'],
    ['nuri90','Neutral','Spain','EV'],['santiago8','Neutral','Chile','KS'],['Joseluna','Positive','Peru','KS'],['alberto','Positive','Francia','OT'],['jgbesq','Negative','Panana','KS'],
    ['sixt93','Negative','Portugal','OT'],['santiago8','Neutral','Chile','KS'],['santiago8','Neutral','Bolivia','PA'],['nico23','Neutral','USA','PA'],['alberto','Positive','USA','KS'],
]

Dic_Autores = { '1':Autores[0],'2':Autores[1],'3':Autores[2],'4':Autores[3],'5':Autores[4],'6':Autores[5],'7':Autores[6],'8':Autores[7],'9':Autores[8],'10':Autores[9],'11':Autores[10],'12':Autores[11],'13':Autores[12],'14':Autores[13],'15':Autores[14],

}


# Create DataFrame
data = pd.DataFrame(Dic_Autores)
 
# Write to CSV file
data.to_csv("Data_del_reto.csv")
 
# Print the output.
#print(data)

# with open('data.csv','w', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(Dic_Autores)

#df = pd.read_csv('Data_del_reto.csv')
df = pd.read_csv('Data_del_reto.csv')


