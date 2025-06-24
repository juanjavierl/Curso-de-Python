""" def escrituras_txt():
    with open("lista_compras.txt", "w") as archivo:
        archivo.write("Lista de compras\n")
        archivo.write("Azucar\n")
        archivo.write("Arroz")
escrituras_txt()

def leer_archivo():
    with open("lista_compras.txt") as archivo:
        print(archivo)
        for dato in archivo:
            print(dato)

leer_archivo() """

import json
datos ={
    'nombre:':'jose',
    'edad':25,
    'activo':True
    }

with open('dato.json','w') as data:
    json.dump(datos, data, indent=4)


with open('dato.json') as data:
    datos = json.load(data)
    #print(datos)
    for c, v in datos.items():
        print(c," - " ,v)

import csv

datos = [
    ['nombre', 'edad', 'estado'],
    ['juan', 25, 'casado']
]

with open("texto.csv","w", newline='') as archivo:
    arch =  csv.writer(archivo)
    arch.writerows(datos)


    