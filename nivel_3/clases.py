import csv
import os
import random

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, sueldo, ci=5555):
        self.nombre = nombre
        self.sueldo = float(sueldo)
        self.__ci = ci

    def __str__(self):
        return f"{self.nombre} gano {self.sueldo} bs"
    
    def to_list(self):
        return [self.nombre, self.sueldo, self.determinar_impuesto()]
    
    @abstractmethod
    def determinar_impuesto(self):
        pass
    
    def mostar_ci(self):
        return self.__ci
    
    def __codigo(self):
        return f"Codigo: {random.randint(100,999)}"
    
    def saludar(self):
        resp = self.__codigo()
        return f"Hola desde la clase padre {resp}"
    
class EmpleadoEventual(Empleado):
    def __init__(self, nombre, sueldo, ci, direccion):
        super().__init__(nombre, sueldo)
        self.ci = ci
        self.direccion = direccion
    def __str__(self):
        return f"El eventual: {self.nombre} - gano: {self.sueldo} su direccion es: {self.direccion}"

    def determinar_impuesto(self):
        mej = ""
        if self.sueldo >= 3000:
            mej = "Si"
        else:
            mej = "No"
        return mej

empleado1  = EmpleadoEventual('jose', 4500, 787787,'Av Velez')
print(empleado1.determinar_impuesto())

# emp_eventual = EmpleadoEventual('jose', 4500, 787787,'Av Velez')
# print(emp_eventual)

class Agenda:
    def __init__(self, archivo='agenda.csv'):
        self.archivo = archivo
        self.inicializar_archivo()


    def inicializar_archivo(self):
        if not os.path.exists(self.archivo):
            with open(self.archivo, mode='w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow(['Nombre', 'Sueldo', 'Paga impuestos'])


    def agregar_contacto(self, contacto):
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(contacto.to_list())
        print("Contacto agregado")


    def listar_contactos(self):
        with open(self.archivo, mode='r', newline='', encoding='utf-8') as file:
            lector = csv.reader(file)
            next(lector)  # Saltar encabezado de titulos
            for fila in lector:
                print(f"Nombre: {fila[0]} | Sueldo: {fila[1]} | Paga impuestos: {fila[2]}")


    def editar_contacto(self, nombre_buscar, nuevo_sueldo):
        contactos = []
        encontrado = False
        with open(self.archivo, mode='r', newline='', encoding='utf-8') as file:
            lector = csv.reader(file)
            encabezado = next(lector)
            for fila in lector:
                if fila[0] == nombre_buscar:
                    # Crear nuevo empleado con el nuevo sueldo
                    empleado_actualizado = Empleado(nombre_buscar, nuevo_sueldo)
                    contactos.append(empleado_actualizado.to_list())
                    encontrado = True
                else:
                    contactos.append(fila)


        if encontrado:
            with open(self.archivo, mode='w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow(encabezado)
                escritor.writerows(contactos)
            print("Contacto editado")
        else:
            print("Contacto no encontrado")


    def eliminar_contacto(self, nombre_buscar):
        contactos = []
        encontrado = False
        with open(self.archivo, mode='r', newline='', encoding='utf-8') as file:
            lector = csv.reader(file)
            encabezado = next(lector)
            for fila in lector:
                if fila[0] != nombre_buscar:
                    contactos.append(fila)
                else:
                    encontrado = True


        if encontrado:
            with open(self.archivo, mode='w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow(encabezado)
                escritor.writerows(contactos)
            return True
        else:
            return False

def main():
    agenda = Agenda()
    while True:
        print(" ********* Mi Agenda ************")
        print("1.- Agregar")
        print("2.- Listar contactos")
        print("3.- Editar un contacto")
        print("4 .-Eliminar")
        print("5.- Salir")

        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            nombre = input("Nombre: ")
            sueldo = input("Suledo: ")
            contacto = Empleado(nombre, sueldo)
            agenda.agregar_contacto(contacto)
        elif opcion == 2:
            agenda.listar_contactos()
        elif opcion == 3:
            nombre = input(" Nombre a editar: ")
            nuevo_sueldo = input("Nuevo sueldo: ")
            agenda.editar_contacto(nombre, nuevo_sueldo)
        elif opcion == 4:
            nombre = input(" Nombre a eliminar: ")
            if agenda.eliminar_contacto(nombre):
                print("Contacto Eliminado ")
            else:
                print("Dato no encontrado")
        elif opcion == 5:
            print("Proceso terminado")
            break
        else:
            print("Error opcion invalida")
            

#main()

""" empleado1 = Empleado()
print(empleado1.determinar_impuesto()) """