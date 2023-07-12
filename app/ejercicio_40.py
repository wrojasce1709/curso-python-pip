# otra forma de hacer el ejercicio

from csv import reader
import matplotlib.pyplot as plt

with open('./app/data.csv','r') as data:
    reader1 = reader(data)
    header = next(reader1)
    data1=[]
    for line in reader1:
        codict=dict()
        for i,j in zip(header,line):
            if 'Country/Territory' in i or 'Population' in i :
                codict[i]=j
        data1.append(codict)

def graficar(data,name):
    result= list(filter(lambda item:item['Country/Territory']==name,data))[0]
    labels=list(result.keys())[1:-1]
    values=list(map(int,list(result.values())[1:-1]))
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
country = input('type country: ').capitalize()
graficar(data1,country)

# python app/ejercicio_40.py