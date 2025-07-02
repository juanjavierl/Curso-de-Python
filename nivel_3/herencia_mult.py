class Telefono:
    """Clase teléfono"""
    def __init__(self,numero):
        self.numero=numero
    def telefonear(self):
        print('llamando')
    def colgar(self):
        print('colgando') 
    def __str__(self):
        return self.numero
    
    def encender(self):
        return "El telefono se encendio"

class Camara:
    "Clase camara fotográfica"
    def __init__(self,mpx):
        self.mpx=mpx
    def fotografiar(self):
        print('fotografiando')        
    def __str__(self):
        return self.mpx
    def encender(self):
        return "La camara se inicio"
    
class Reproductor:
    "Clase Reproductor Mp3"
    def __init__(self,capcidad):
        self.capacidad=capcidad
    def reproducirmp3(self):
        print('reproduciendo mp3')                  
    def reproducirvideo(self):
        print('reproduciendo video')                  
    def __str__(self):
        return self.capacidad

    def encender(self):
        return "El reprodutor se encendio"	

class Movil(Telefono, Camara, Reproductor):
    def __init__(self,numero,mpx,capacidad):
        Telefono.__init__(self,numero)
        Camara.__init__(self,mpx)
        Reproductor.__init__(self,capacidad)
    def encender(self):
        return "El movil se encendio"
    def __str__(self):
        return f"Número: {Telefono.__str__(self)}, Cámara: {Camara.__str__(self)},Capacidad: {Reproductor.__str__(self)}"


mimovil=Movil("645234567","5Mpx","1G")
print(mimovil)

#print(issubclass(Movil,Telefono))

telf = Telefono("78458754")
cam = Camara("10px")

def encenser_dispositivo(cam):
    return cam.encender()

print(encenser_dispositivo(cam))