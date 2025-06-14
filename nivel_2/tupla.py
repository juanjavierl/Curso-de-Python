tupla = (46, 35, 22, 61, 40.5, "Maria", True, (1, 2, 3))
tupla[0]
valor = 22
if valor in tupla:
    print("Valor encontrado")
else:
    print("Valor no existe")

print(len(tupla)) 

""" mi_tupla = (10, 20, 30, 40)

for valor in mi_tupla:
    print(valor) """

""" for indice in range(0,len(mi_tupla)):
    print(mi_tupla[indice] + 5) """





#datos_estudiente()

def verificar_orden(tupla):
    for i in range(len(tupla) -1):
        if tupla[i] > tupla[i+1]:
            return False
    return True


mi_tupla = (1,2,3,4,5,6)
print(verificar_orden(mi_tupla))