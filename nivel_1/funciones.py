""" public void sumar(){
    bloque de instrucciones
} """

""" def saludo(nombre):
    #bloques de codigo
    print(nombre.upper())
    print("Hola desde mi funcion")

nom = input("Escriba su nombre: ")
saludo(nom) """

""" def mi_funcion(nombre, apellido, edad=0): 
    nombre_completo = nombre + apellido 
    #print(nombre_completo, "Tiene edad: ", edad)
    return f"{nombre_completo} Tiene edad: {edad}"

persona = mi_funcion("jose ", " perez", 25)
print(persona.upper())
#mi_funcion("jimernez ", " carlos") """

#!5 proceso 5*4*3*2*1 = 120

""" def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num

print(factorial(5)) #salida sera: >>120 """

""" def saludo(nombre):
    #bloques de codigo
    print(nombre.upper())
    print("Hola desde mi funcion")

def main():
    nom = input("Escriba su nombre: ")
    saludo(nom)
main() """


def factorial(num):
    fac = 1
    for i in range(1,num+1, 1):
        fac = fac * i
    return fac
#print(factorial(5))
def calcular(n, r):
    n1 = factorial(n)
    r1 = factorial(r)
    n_r1 = factorial(n-r)
    c = n1 // (r1 * (n_r1))
    return c

def main():
    n = int(input("Ingrese al valor de N: "))
    r = int(input("Ingrese al valor de R: "))
    print(calcular(n,r))

main()


def determinar(invertida):
    #print(palabra[5])
    invertida = palabra[::-1]
    if palabra.lower() == invertida.lower():
        print("Palimdromo")
    else:
        print("No es palimdromo")

palabra = input("Escriba una palabra: ")
determinar(palabra)



