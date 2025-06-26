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

""" with open('dato.json','w') as data:
    json.dump(datos, data, indent=4)


with open('dato.json') as data:
    datos = json.load(data)
    #print(datos)
    for c, v in datos.items():
        print(c," - " ,v) """

import csv

def escritura_datos():
    datos = [
        ['nombre', 'edad', 'estado'],
        ['juan', 25, 'casado'],
        ['maria',30, 'soltero'],
        ['jose', 15, 'soltero'],
        ['pedro',20, 'soltero']
    ]

    with open("texto.csv","w", newline='') as archivo:
        arch =  csv.writer(archivo)
        arch.writerows(datos)

def verificar_edades(edad):
    estado_edad = ""
    if edad >= 18:
        estado_edad = "Mayor de Edad"
    else:
        estado_edad = "Menor de edad"
    return estado_edad


def prosesar_datos():
    with open("texto.csv","r", newline='') as file:
        leer = csv.reader(file)
        next(leer)
        contar_registros = 0
        casados, solteros, suma_edades = 0, 0, 0
        for datos in leer:
            #print(datos)
            contar_registros+=1
            suma_edades += int(datos[1])
            if datos[2].strip().lower() == 'casado':
                casados +=1
            else:
                solteros+=1
            verificar = verificar_edades(int(datos[1]))
            print(f"{datos[0]} es: {verificar}")
        print(f"Total de registros: {contar_registros}")
        print(f"La suma de las edades es: {suma_edades}")
        print(f"Total casados: {casados}")
        print(f"total Solteros: {solteros}")
prosesar_datos() 