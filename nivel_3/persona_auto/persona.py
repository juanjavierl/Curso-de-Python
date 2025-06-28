class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.__ci = ci

    def __str__(self):
        return self.nombre
    
    def levantarse(self):
        return "Me estoy levantando"
    
    def aumentar_velocidad(self, coche1, velocidad):
        aumentar = coche1.acelerar(velocidad)
        return aumentar