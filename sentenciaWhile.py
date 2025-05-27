


""" suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("La Suma de los dígitos es:", suma) """

""" numero = int(input("Ingrese un numero: "))
suma = 0
while numero > 0:
    print(numero, end=" ")
    suma = suma + numero
    numero = numero - 1
print("\nLa suma es: ",suma) """


""" numero = 1
while numero <= 5:# True
    print(f"\nTabla del {numero}")
    multiplicador = 1
    while multiplicador <= 10:#True
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador = multiplicador + 1
    numero = numero + 1 """


numero = int(input("Ingrese un valor"))
contadorNumeros = 0
contPares = 0
sumaPares = 0
promedio = 0
contImpares = 0
if numero > 0:
    while numero > 0:
        contadorNumeros +=1
        if numero % 2 == 0:
            contPares = contPares + 1
            sumaPares = sumaPares + numero
        else:
            contImpares = contImpares + 1
        numero = int(input("Ingrese un valor: "))
else:
    print("Error de valor")

print("total numeros Pares: ", contPares)
print("La suma de los num pares es:", sumaPares)
print("El promedio de los num pares es: ",sumaPares//contPares)

print(f"total de numeros impares: {contImpares}")

print("Total de digitos: ", contadorNumeros)





