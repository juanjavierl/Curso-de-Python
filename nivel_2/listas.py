mi_lista = [2,4,6,8,10,"hola", True, ['a','e','i','o','u']]
mi_lista[5]="Bienvenidos"
print(mi_lista)
""" mi_lista = [2,4,6,8,10,"hola", True, ['a','e','i','o','u']]

print(type(mi_lista))
for valor in mi_lista:
    print(valor, end=" ") """

""" for i in range(0, len(mi_lista), 1):
    print(mi_lista[i], end=" ") """


""" def invertir_cadena(texto):
    palabras = texto.split(" ")
    textos_invertidas = []
    for palabra in palabras:
        palabras_invertidas = ""
        for letra in palabra:
            palabras_invertidas = letra + palabras_invertidas
        textos_invertidas.append(palabras_invertidas) 
        #print(textos_invertidas) 
    resultado = " ".join(textos_invertidas)
    print(resultado)

invertir_cadena("Hola como estas") """

import random
def generar_lista(tamanio):
    lista = []
    contador = 0
    while contador < tamanio:
        num_aleatorio = random.randint(1,100)
        if num_aleatorio % 3 == 0:
            lista.append(num_aleatorio)
            contador+=1
    return lista

def suma_lista(lista):
    """ suma = 0
    for valor in lista:
        suma = suma + valor
    return suma """
    return sum(lista)

def min_valor(lista):
    valor_minimo = min(lista)
    return valor_minimo

def main():
    tamanio=int(input("Ingrese el tamanio de la lista: "))
    print(generar_lista(tamanio))
    print(suma_lista(generar_lista(tamanio)))
    print(min_valor(generar_lista(tamanio)))
main()





