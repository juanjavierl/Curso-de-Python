import json
class Vehiculo:

    def __init__(self, ruedas, color, modelo=2005):
        self.ruedas = ruedas
        self.color = color
        self.__modelo = modelo
        #return f"Auto con {self.ruedas} ruedas de color: {self.color}"

    def __str__(self):
        return f"Auto con {self.ruedas} ruedas es de color: {self.color}"

    def __getattr__(self):
        return self.color

    def setattr(self, NewColor):
        self.color = NewColor
        return self.color

    def otro(self):
        contador = 0
        self.color

    def datos_json(self):
        datos = {
            'color':self.color,
            'ruedad':self.ruedas
        }
        return json.dumps(datos)
    
    def acelerar(self, velocidad):
        return f"El choche esta a una velocidad de: {velocidad} k/h"
