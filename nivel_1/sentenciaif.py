""" numero = 0
if numero > 0:
    print("El numero es mayor que cero")
else:
    print("El numero es negativo")

nota = int(input("Ingrese su nota: "))
if nota > 0 and nota <= 100:
    if nota > 95:
        print("El estudiante es muy bueno")
    else:
        if nota > 65:
            print("El estudiante es bueno")
        else:
            if nota > 50:
                print("El estudiante es regular")
            else:
                print("El estudiante es malo")
else:
    print("Error nota invalida") """


""" compra = int(input("Ingrese la compra: "))
if compra > 2500:
    descuento = compra * 0.20
elif compra > 1500:
    descuento = compra * 0.10
elif compra > 600:
    descuento = compra * 0.05
else:
    descuento = 0
total = compra - descuento
#print("La compra", compra, "Tiene un descuento: ", descuento, "Total a pagar: ", total)
print(f"La compra {compra} Tiene un descuento: {descuento} total a pagar: {total}")
 """

dia=int(input('INGRESE UN NUMERO CORRESPONDIENTE AL DIA DE LA SEMANA  :'))
if dia>=1 and dia<=7:
    if dia==1:
        print('el dia es LUNES')
    elif dia==2:
        print('el dia es MARTES')
    elif dia==3:
        print('el dia es MIERCOLES')
    elif dia==4:
        print('el dia es JUEVES')
    elif dia==5:
        print('el dia es VIERNES')
    elif dia==6:
        print('el dia es SABADO')
else:
    print("Error dato invalido")
