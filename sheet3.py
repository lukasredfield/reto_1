""" HOJA DE EXPERIMENTO PARA PROBAR DISTINTOS TIPOS DE LISTAS Y DICCIONARIOS """

import pandas as pd


Lista_de_autores = [
    ['Joseluna','sixt93','alberto','carlosz','jgbesq','nuri90','santiago8','Joseluna','alberto','jgbesq','sixt93','santiago8','santiago8','nico23','alberto'],
['Positive', 'Negative','Neutral'],['Ecuador', 'Colombia','Francia','USA','UK','Spain','Chile','Peru','Panama','Portugal','Chile','Bolivia'],['PA','CA','OT','EV','KS']
]

Lista_de_autores = [
    ['Joseluna','sixt93','alberto','carlosz','jgbesq','nuri90','santiago8','Joseluna','alberto','jgbesq','sixt93','santiago8','santiago8','nico23','alberto'],
['Positive', 'Negative','Neutral'],['Ecuador', 'Colombia','Francia','USA','UK','Spain','Chile','Peru','Panama','Portugal','Chile','Bolivia'],['PA','CA','OT','EV','KS']
]

Autores = [
    ['Joseluna','Positive','Ecuador','PA'],['sixt93','Negative','Colombia','CA'],['alberto','Positive','Francia','OT'],['carlosz','Negative','USA','OT'],['jgbesq','Negative','UK','PA'],
    ['nuri90','Neutral','Spain','EV'],['santiago8','Neutral','Chile','KS'],['Joseluna','Positive','Peru','KS'],['alberto','Positive','Francia','OT'],['jgbesq','Negative','Panana','KS'],
    ['sixt93','Negative','Portugal','OT'],['santiago8','Neutral','Chile','KS'],['santiago8','Neutral','Bolivia','PA'],['nico23','Neutral','USA','PA'],['alberto','Positive','USA','KS'],
]

Dic_Autores = { '1':Autores[0],'2':Autores[1],'3':Autores[2],'4':Autores[3],'5':Autores[4],'6':Autores[5],'7':Autores[6],'8':Autores[7],'9':Autores[8],'10':Autores[9],'11':Autores[10],'12':Autores[11],'13':Autores[12],'14':Autores[13],'15':Autores[14],

}

# Dic2_Autores = { 'Author':Lista_de_autores[0],'Sentiment':Lista_de_autores[1]

# }

 
# # initialise data dictionary.
# data_dict = {'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              
#              'Gender': ["Male", "Female", "Female", "Male",
#                         "Male", "Female", "Male", "Male",
#                         "Female", "Male"],
              
#              'Age': [20, 21, 19, 18, 25, 26, 32, 41, 20, 19],
              
#              'Annual Income(k$)': [10, 20, 30, 10, 25, 60, 70,
#                                    15, 21, 22],
              
#              'Spending Score': [30, 50, 48, 84, 90, 65, 32, 46,
#                                 12, 56]}
 
# # Create DataFrame
# data = pd.DataFrame(data_dict)
 
# # Write to CSV file
# data.to_csv("Customers.csv")
 
# # Print the output.
# print(data)

# Author = ['Joseluna','sixt93','alberto','carlosz','jgbesq','nuri90','santiago8','Joseluna','alberto','jgbesq','sixt93','santiago8','santiago8','nico23','alberto']
# Sentiment = ['Positive', 'Negative','Neutral']
# Country = ['Ecuador', 'Colombia','Francia','USA','UK','Spain','Chile','Peru','Panama','Portugal','Chile','Bolivia']
# Theme = ['PA','CA','OT','EV','KS']

# initialise data dictionary.
data_dict = {'Author': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              
             'Gender': ["Male", "Female", "Female", "Male",
                        "Male", "Female", "Male", "Male",
                        "Female", "Male"],
              
             'Age': [20, 21, 19, 18, 25, 26, 32, 41, 20, 19],
              
             'Annual Income(k$)': [10, 20, 30, 10, 25, 60, 70,
                                   15, 21, 22],
              
             'Spending Score': [30, 50, 48, 84, 90, 65, 32, 46,
                                12, 56]}
 
# Create DataFrame
data = pd.DataFrame(data_dict)
 
# Write to CSV file
data.to_csv("Customers.csv")
 
# Print the output.
print(data)