import main

# Al ejcutar example.py tambien se esta ejecutando main.py.
#print("example => ",main.data) 

"""Este comportamiento no es el adecuando, simplemente por importar un modulo se empiesa a ejecutar, para resolver el problema se necesita (modularizar)
- Una forma de modularizar es incorporar a 'data' dentro de una funcion directamente en main.py 
"""
print(main.data) # desde este punto ya se encuentra controlado main.data
main.run()
# python app/example.py