
#datos['carrera'] = 'Sistemas'
#print(datos.get('edades', 'No existe'))
#print('nombres' in datos)
#del datos['edad']
#print(datos.items())
""" valor = datos.pop(100, "No existe valor")

informacion = datos.copy()
nuevo = informacion.popitem()
print(nuevo)
print(informacion) """


""" def mi_diccionario():
    datos = {
        'nombre':'jose',
        'edad':25,
        'estado':True,
        10:'Diez'
    }

  for i in datos:
        print(i , ": ", datos[i])

    for clave, valor in datos.items():
        print(clave, ": ", valor)

mi_diccionario() """


""" datos = {
        'nombre':'jose',
        'edad':25,
        'estado':True,
        10:'Diez',
        'deportes':{
            1:'ajedrez',
            2:'natacion',
            3:'futbol',
            4:['1', 'uno']
        }
    }


def llenar_datos(estudiante):
    estudiante['nombre'] = input("ingrese su nombre: ")
    estudiante['edad'] = int(input("Ingrese su edad: "))
    estudiante['carrea'] = input("Ingrese su carrera: ")
    estudiante['estatura'] = float(input("Estatura: "))
    return estudiante

def mostrar_datos(estudiante):
    for clave, valor in estudiante.items():
        print(clave, ": ", valor)

def main():
    datos = {}
    estudiantes = llenar_datos(datos)
    mostrar_datos(estudiantes)

main() """

def optener_alumnos():
    alumnos = {
        0: {'nombre': "Juan David", 'notas': [60, 55, 75]},
        1: {'nombre': "Rodrigo", 'notas': [50, 30, 45]},
        2: {'nombre': "David", 'notas': [70, 55, 75]},
        3: {'nombre': "Jhannet", 'notas': [60, 65, 85]},
        4: {'nombre': "Beto", 'notas': [25, 50, 35]}
    }
    return alumnos

def suma_y_promedio(notas):
    total = sum(notas)
    promedio = total // len(notas)
    return total, promedio

def obtener_estado(promedio):
    estado = ""
    if promedio >= 61:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    return estado

def mostrar_datos(nombre, notas, total, promedio, estado):
    print(f"{nombre} Notas: {notas}  Total: {total} Promedio: {promedio} {estado}")


def estudiantes():
    alumnos = optener_alumnos()
    # Recorrer cada alumno y mostrar su información
    for alumno_id in alumnos:
        alumno = alumnos[alumno_id]
        nombre = alumno['nombre']
        notas = alumno['notas']
        
        total, promedio = suma_y_promedio(notas)
        estado = obtener_estado(promedio)
        mostrar_datos(nombre, notas, total, promedio, estado)
        
        # Mostrar información
estudiantes()
