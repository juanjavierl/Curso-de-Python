""" import random
def generar_contraseña(longitud):
    letras = 'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    contraseña = ''
    for i in range(longitud):
        contraseña += random.choice(letras)
    return contraseña

# Función para pedir la longitud al usuario
def obtener_longitud():
    entrada = input("Longitud de la contraseña (presiona Enter para usar 6): ")
    if entrada.strip().isdigit():
        return int(entrada)
    else:
        return 6

# Función principal
def main():
    longitud = obtener_longitud()
    contraseña = generar_contraseña(longitud)
    print("\nContraseña generada es:", contraseña)
# Ejecutar el programa
main() """

def operaciones(valor, saldo):
    if valor==1:
        monto = float(input("Inserte el monto a Depositar: "))
        saldo = saldo + monto
        print(f"Usted deposito: ", monto)
        return saldo
            
    elif valor==2:
        monto = float(input("Ingrese Monto del retiro: "))
        if monto<= saldo:
            saldo = saldo - monto
            print(f"Retiro exitoso de: ", monto)
            return saldo
        else:
            print("Su Saldo es insuficiente")
            return saldo
    return saldo
                   
def validar(opcion):
     if opcion.isdigit():
        opcion = int(opcion)
        if opcion in range(0,3):
            return opcion
        else:
            print("elija una opcion valida...")
            menu()   

def menu():
    print("***********************************************")
    print("*************CAJERO AUTOMÁTICO*****************")
    print("1. Depositar")
    print("2. Retirar")
    print("0. Salir")
    op = input(" Elija una opción: ")
    return op

def main():
    saldo = 0.0
    opcion = menu()
    valor = validar(opcion)
    while valor!= 0:
        saldo= operaciones(valor, saldo)
        print("***********************")
        opcion=input("elija una opcion: ")
        valor = validar(opcion)
    print("Gracias por su preferencia.Su Saldo Actual es: ", saldo)
main()