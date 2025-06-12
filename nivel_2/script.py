from saludos import *
from funciones import *
#import saludos as s

#Llamada a un paquete
from paquete1.hola import saludar
from paquete1.dadesdidas import *

from paquete1.subpaquete.funciones_matematicas import cuadrado
bienvenida("jose")
print(sumar(3,6))

print(multiplicar(5, 5))

saludar("Maria")

nombre = "Maria"

despedida(nombre)

print("El cuadrado del numero es: ", cuadrado(9))