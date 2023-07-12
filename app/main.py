"""
la importacion de modulos puede contener, funciones, diccionarios, listas, tuplas, variables que se pueden importar de un archivo a otro.
Los modulos permiten modularizar y reutilizar una funcion que tenga utilidades.

main.py = principal es el que se puede ejecutar como un scripts = secuencias, cualquier archivo de python se considera modulo, esto nos permite modularizar nuestra aplicacion y reutilizar codigo desde archivos.


          EJEMPLOS DE IMPORTACION DE FUNCIONES
importacion = utils.get_population()
print(importacion)

keys, values = utils.get_population()
print(a,b)

print(utils.wilder) # modalizar nuestra aplicacion y reutilizar codigo desde archivos


data = [
  {
    "Country": "Colombia",
    "population": 300
  },
  {
    "Country": "Argentina",
    "population": 250
  },
  {
    "Country": "Brazil",
    "population": 600
  }
]
"""

import utils
import read_csv
import charts

# Modulos creado a traves de una funcion

def run(): # funciopn que corre las demas funciones
  data = read_csv.read_csv('data.csv') # transforma en forma de diccionario
  data = list(filter(lambda item : item['Continent'] == "South America", data)) # filtro de csv=data por columna
  countries = list(map(lambda i: i['Country/Territory'], data)) # litro por la informacion de paises
  percentages = list(map(lambda x: x["World Population Percentage"], data)) # filtro con inf de los porcentajes
  charts.generate_pie_chart(countries, percentages) # renderizar un pai_chart
  country = input("ingrese el pais: ").capitalize()
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)



if __name__ == '__main__':
  run()
  
  


"""
Hacer que el archivo principal mainpy se puede ejecutar desde un scrip desde la terminal Shell
- el modulo example controla la ejecucion de main.py, la primera forma de correr el programa es corriendo el modulo python app/example.py directamente desde main.py
- la segunda forma de correr el archivo es hacerlo con dualidad, esto quiere decir que se puede correr el programa desde main.py o desde example.py a traves de: if  __name__ == "__main__": esta if le dice al archivo main.py que ejecute la funcion run() desde la terminal pero si es ejecutado desde otro archivo esto no se va a ejecutar



if  __name__ == "__main__":
run()
 
# python app/main.py
# python app/example.py
""" 