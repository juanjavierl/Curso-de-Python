class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.sueldo = float(input("Ingrese su sueldo: "))

    def __str__(self):
        return f"{self.nombre} gano {self.sueldo} bs"
    
    def otr_metod(self, valor):
        pass
    
    def determinar_impuesto(self):
        mej = f""
        if self.sueldo >= 3000:
            mej = f"{self.nombre} Si Paga impuestos"
        else:
            mej = f"{self.nombre} No paga impuestos"
            self.otr_metod(mej)
        return mej
    


empleado1 = Empleado()
print(empleado1.determinar_impuesto())