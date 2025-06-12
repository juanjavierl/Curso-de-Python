""" def sumar(a, b):
    return a + b

print(sumar(10, 20)) """

#resultado = lambda a, b: a + b
#print(resultado(10, 5))


#print((lambda a, b: a + b)(5,7))

# Evaluar si un número es par

# es_par = lambda x: x % 2 == 0
# print(es_par(15))  # True


# numeros = [1, 2, 3, 4]
# cuadrados = list(map(lambda x: x**2, numeros))
# print(cuadrados)  # [1, 4, 9, 16]

# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  # [2, 4]
""" def saludar(nombre, edad):
    def saludar_interna():
        print(f"Hola, {nombre}! tiene {edad} anios")

    saludar_interna()  # Llamar a la función interna

saludar("Jose", 15) # La salida es "Hola, Jose!"

#Evalular al nota de un estudiante segun su calificacion 
def evaluar_alumno(nombre, nota):
    def evalular_nota():
        if nota > 9:
            return "Muy bueno"
        elif nota > 7:
            return "Bueno"
        elif nota > 5:
            return "Regular"
        else:
            return "Reprobado"
    desentenio = evalular_nota()
    return f"El alumno: {nombre} su nota es:{nota} desempeño es: {desentenio}"

print(evaluar_alumno("Jose",5)) """


def funcion_a(funcion_b):
    def funcion_c(a, b):
        print(f"valor de a: {a}, valor de B {b}")
        resp = funcion_b(a, b)
        print("Al tarminar de ejecutar")
        return resp
    return funcion_c

@funcion_a
def saludar():
    print("hola un saludo")
saludar()

@funcion_a
def sumar(a, b):
    return a + b

print(sumar(10,15))




