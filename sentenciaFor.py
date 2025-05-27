
""" for i in range(30, -1, -3):
    print(i) """

""" multiplicador=int(input("multiplicador: "))
for i in range(1, multiplicador+1, 1):  # límite hasta el número dado
    for j in range(1, 11, 1):  # Multiplicador (1 al 10)
        print(i, " x " ,j, " = ",i * j) # muestra la tabla
    print() # para cuando termine el segundo for hago un salto """

""" fila = int(input("Num Fila: "))
cols = int(input("Num Columnas: "))
for i in range(fila):
    for j in range(cols):
        print(j, end=" ")
    print() """


tam = int(input("Tamanio : "))
for i in range(tam):
    for j in range(tam):
        if i == j or i+j == tam-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


""" for i in range(1, 10+1, 1):
    if i == 5:
        pass #break continue
    print(i) """

