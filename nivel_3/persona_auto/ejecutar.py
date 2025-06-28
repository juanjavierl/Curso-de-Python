from vehiculo import Vehiculo
from persona import Persona
def main():
    coche1 = Vehiculo(12, 'Verde')
    #print(coche1.acelerar(80))

    persona1 = Persona('Pedro', 'Perez', 5454548)
    #print(persona1)

    print(persona1.aumentar_velocidad(coche1, 160))

main()