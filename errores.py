""" try:
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    resp = dividendo // divisor
    print(resp)
except ValueError:
    print("Error de valor")
except ZeroDivisionError:
    print("Error de divicion ") """

""" try:
    resultado = 10 + 5
    print(resultado)
except TypeError:
    print("¡No puedes mezclar texto con números!") """

#manejo de librerias

""" import random
numero_aleatorio = random.randint(1, 10)
intentos = 3
for i in range(1,intentos+1):
    try:
        adivina = int(input(f"Intentos: {i} adivina el numero: entre 1 - 9: "))
        if adivina == numero_aleatorio:
            print("Adivinaste el numero..")
            break
        elif adivina < numero_aleatorio:
            print("Muy bajo")
        else:
            print("Muy alto")
        if i < intentos:
            print(f"Te quedan {intentos - i} intentos")
        else:
            print("Lo siento perdiste")
    except ValueError:
        print("Datos invalidos ") """


""" import math

potencia = math.pow(2,3)
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(potencia) """

""" import os
print(os.getcwd())  # Muestra el directorio de trabajo actual
archivos = os.listdir(".")  # Lista archivos del directorio actual
print(archivos) """

from datetime import datetime
""" fecha_hora_actual = datetime.now()

Fecha=fecha_hora_actual.strftime("Dia %A mes %B %Y-%m-%d %H:%M")
print(fecha_hora_actual.date().month)
print(Fecha) """

fecha = "2025-06-02 20:05"
fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
print(fecha.hour)



fecha1 = datetime(2026, 5, 10, 20, 14)
fecha2 = datetime(2025, 6, 1, 20, 14)
if fecha1 < fecha2:
    print("La fecha1 es menor")
else:
    print("La fecha1 es mayor")









