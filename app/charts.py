# libreria para la visualizacion con python: https://matplotlib.org/
# https://platzi.com/blog/matplotlib/
# https://platzi.com/cursos/matplotlib-seaborn/

# as plt es para crear un sinomimo corto del nombre de la importacion de libreria
import matplotlib.pyplot as plt
"""
def generate_bar_chart():
  labels = ['a', 'b', 'c']
  values = [10, 20, 40]
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  generate_bar_chart()
"""


def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{name}.png") # guardar archivo con nombre
  plt.close() # cerrar el programa sin que se detenga


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig("pie.png") # guardar y cerrar el programa sin que se detenga
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 150]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

# python app/charts.py
