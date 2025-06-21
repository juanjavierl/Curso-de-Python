""" multi_list = [
    [1, 2, 3, 4, 5],
    ['a','b','c','d','c'],
    [10, 20,30,40,50]
]

multi_list.append([101, 201,310,410,510])
for fila in multi_list:
    for columna in fila:
        print(columna, end=" ")
    print()  """


def multi_lista():
    fila = int(input("Ingrese el num. de filas: "))#ingresamos un número de filas
    columna = int(input("Ingrese el num. de Columnas: "))#número de columnas
    multi_lista = [] #inicializamos una lista vacía
    for f in range(0, fila,1):
        lista = []
        for c in range(0, columna, 1):
            print("Ingrese valor en el indice:",f," : ",c)
            valor = int(input())
            lista.append(valor)  
        multi_lista.append(lista)
    return multi_lista

def mostrar_lista(matriz):
    for fila in matriz:
        print(fila)

def sumar_diagonal_principal(matriz):
    suma = 0
    for fila in range(len(matriz)):
        for cols in range(len(matriz)):
            if fila == cols:
                suma = suma + matriz[fila][cols]
    return suma

def suma_dig_secundrio(matriz):
    pass

def main():
    matriz = multi_lista()#llamada a la función
    mostrar_lista(matriz)
    print("La suma de su diagonal principal es: ",sumar_diagonal_principal(matriz))
main()