from bomber import Bomberman

class Vehiculo:
    def __init__(self, _modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso):
        self.modelo = _modelo
        self.color = _color
        self.marca = _marca
        self.velocidad = _velocidad
        self.cant_pasajeros = _cant_pasajeros
        self.peso = _peso
    
    def encender(self):
        return print("Encender")
    
    def apagar(self):
        return print("Apagar")
        
class Aereo(Vehiculo, Bomberman): # herencia multiple
    def __init__(self, _modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso, _nro_vuelo, _hr_vuelo, _hr_salida, _name, _pos_x, _pos_y):
        Vehiculo.__init__(_modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso) # herencia
        Bomberman.__init__(self, _name, _pos_x, _pos_y)
        self.nro_vuelo = _nro_vuelo
        self.hr_vuelo = _hr_vuelo
        self.hr_salida = _hr_salida
        
        
        
    def elevar(self):
        print("Elevar")

    def aterrizar(self):
        print("Aterrizar")

class Terrestre(Vehiculo):
    def __init__(self, _modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso, _nro_puertas, _cant_carga):
        super().__init__(_modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso)
        self.nro_puertas = _nro_puertas
        self.cant_carga = _cant_carga
    
    def marchar(self):
        print("Marchar")

    def frenar(self):
        print("Frenar")
    
class Maritimo(Vehiculo):
    def __init__(self, _modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso, _cap_carga):
        super().__init__(_modelo, _color, _marca, _velocidad, _cant_pasajeros, _peso)
        self.cap_carga = _cap_carga
        
    def navegar(self):
        print("Navegar")
        
        
aereo1 = Aereo("Airnav 1", "Negro", "Speedsound", "300 km/h", 150, "2 ton", 3563, "2:00", "12:00", "", 50, 50)
aereo2 = Aereo("Airnav 2", "Blanco", "Speedster", "5000 km/h", 2, "1 ton", 53, "5:00", "15:00")

terrestre1 = Terrestre("Terreneitor 1", "Blanco", "4x4", "150 km/h", 5, "500 kg", 5, 10)
terrestre2 = Terrestre("Terreneitor 3", "Azul", "Busneitor", "100 km/h", 20, "1 ton", 2, 100)

maritimo1 = Maritimo("Barco 1", "Blanco", "Waterfall", "24 mil/h", 450, "1 ton", "1 ton")
maritimo2 = Maritimo("Acuaton", "Negro", "Twister", "34 mil/h", 250, "1 ton", "1 ton")
