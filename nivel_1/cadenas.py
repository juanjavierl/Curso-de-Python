nombre = "Python"
#print(nombre[0])
#print(type(len(nombre)))
""" for i in range(0, len(nombre), 1):
    print(nombre[i], end="") """

""" for letra in nombre:
    print(letra, end="") """

# Solicita al usuario una cadena y una letra
""" texto = input("Ingresa una cadena de texto: ")
caracter = input("Ingrese la letra que deseas contar: ")
# Validar que ingresó exactamente una letra

contador = 0
for letra in texto:
    if letra == caracter:
        contador += 1
print("La letra:", caracter, "se repite:", contador) """







""" texto = input("Ingrese un texto: ")
invertida = ""
for letra in texto:
    print(letra)
    invertida = letra + invertida
print(invertida.upper()) """


""" texto = input("Ingrese un texto: ")
invertida = ""
for letra in range(len(texto)-1, -1, -1):
    #print(letra)
    invertida = invertida + texto[letra]
print(invertida.upper()) 

oso panda   === oso panda
"""

palabra = input("Escriba una palabra: ")
print(palabra[5])
invertida = palabra[::-1]
if palabra.lower() == invertida.lower():
    print("Palimdromo")
else:
    print("No")
