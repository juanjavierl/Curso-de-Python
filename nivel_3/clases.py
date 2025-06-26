class Vehiculo:
    ruedas = 2
    color = "rojo"

    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color
        #return f"Auto con {self.ruedas} ruedas de color: {self.color}"

    def __str__(self):
        return f"Auto con {self.ruedas} ruedas de color: {self.color}"

    def otro(self):
        contador = 0
        self.color
    
    
choche1 = Vehiculo(12, 'Verde')
print(choche1)

""" choche2 = Auto()
print(choche2.crear_coche(2, 'Blanco')) """
