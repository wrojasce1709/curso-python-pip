# https://www.kaggle.com/
# https://www.w3schools.com/python/python_file_open.asp


#LECTOR DEL CSV

import csv
"""
def read_csv(path):
  # with open("./text.txt", "w+") as file:
  with open(path, 'r') as csvfile: 
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      print('***' * 5)
      print(row)
"""
# funcion abrir archivo
def read_csv(path):
  with open(path, 'r') as csvfile:
    # reader() es iterador, lector de archivo
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader) # header = encabezado de columna, se itera manualmente para obetener la primera columna que va hacer la clave para el diccionario
    
    # Transformar archivo en un formato de diccionario
    data = []
    for row in reader:
      iterable = zip(header, row) # unir column y row = direct
      #print(list(iterable)) # Convertir en lista
      country_dict ={key: value for key, value in iterable}
      data.append(country_dict)
      
    return data


    
# correr archivo como script desde la terminal    
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

# python app/read_csv.py

"""
import csv

def reader_csv(path):
with open(path, ‘r’) as csvfile:
reader = csv.reader(csvfile, delimiter= ‘,’)
header = next(reader)
data = []
for row in reader:
iterable = zip(header, row)
prueba =dict((iterable)) # otra forma de convertir el archivo a diccionrio
data.append(prueba)
return data
if name == ‘main’:
data = reader_csv(‘d:\prueba\propython\world_population.csv’)
print (data)
"""

"""
EJERCICIO

Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

#main.py
import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter = ',')
      total = [int(row[1]) for row in reader]
      
   return sum(total)

response = read_csv('./data.csv')
print(response)

#data.csv

Administration,200
Marketing,201
Purchasing,114
Human Resources,203
Shipping,121
IT,103
Public Relations,204
Sales,145
Executive,100
Finance,108
"""