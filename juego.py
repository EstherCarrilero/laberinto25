# Archivo que contiene el juego del laberinto

class ElementoMapa:
    """Clase base para los elementos del laberinto."""
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    def esPared(self):
        return True

class Puerta(ElementoMapa):
    """Representa una puerta que conecta habitaciones."""
    def __init__(self, abierta=False):
        self.abierta = abierta
    
    def esPuerta(self):
        return True
    
    def estaAbierta(self):
        return self.abierta
    
    def abrir(self):
        self.abierta = True
    
    def cerrar(self):
        self.abierta = False

class Habitacion:
    """Representa una habitación en el laberinto con elementos en las 4 direcciones."""
    def __init__(self, numero):
        self.numero = numero
        self.elementos = {
            'norte': None,
            'sur': None,
            'este': None,
            'oeste': None
        }
    
    def establecerElemento(self, direccion, elemento):
        self.elementos[direccion] = elemento
    
    def obtenerElementoOr(self, direccion):
        return self.elementos[direccion]
    
    def esHabitacion(self):
        return True

class Creator:
    """Factory Method para crear el laberinto y sus elementos."""
    
    def fabricarNorte(self):
        return Pared()
    
    def fabricarSur(self):
        return Pared()
    
    def fabricarEste(self):
        return Pared()
    
    def fabricarOeste(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def crearLaberinto2HabitacionesFM(self, juego):
        """Crea un laberinto con 2 habitaciones conectadas por una puerta."""
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        
        # Crear paredes y puerta
        norte = self.fabricarNorte()
        sur = self.fabricarSur()
        este = self.fabricarEste()
        oeste = self.fabricarOeste()
        puerta = self.fabricarPuerta()
        
        # Configurar habitaciones
        hab1.establecerElemento('norte', norte)
        hab1.establecerElemento('sur', puerta)
        hab1.establecerElemento('este', este)
        hab1.establecerElemento('oeste', oeste)
        
        hab2.establecerElemento('norte', puerta)
        hab2.establecerElemento('sur', sur)
        hab2.establecerElemento('este', este)
        hab2.establecerElemento('oeste', oeste)
        
        # Guardar en el juego
        juego.laberinto = [hab1, hab2]

class Juego:
    """Clase principal del juego del laberinto."""
    def __init__(self):
        self.laberinto = []

    def crearLaberinto2HabitacionesFM(self, fm):
        """Crea el laberinto utilizando el Factory Method especificado."""
        fm.crearLaberinto2HabitacionesFM(self)
    
    def obtenerHabitacion(self, numero):
        """Obtiene una habitación por su número."""
        for hab in self.laberinto:
            if hab.numero == numero:
                return hab
        return None

#PRUEBA DEL JUEGO
# Crear el juego y el factory method
juego = Juego()
fm = Creator()

# Crear el laberinto con el Factory Method
juego.crearLaberinto2HabitacionesFM(fm)

# Obtener habitaciones y verificar sus elementos
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)

print("Habitación 1:")
print("Norte es pared:", hab1.obtenerElementoOr('norte').esPared())
print("Sur es puerta:", hab1.obtenerElementoOr('sur').esPuerta())
print("Puerta está abierta:", hab1.obtenerElementoOr('sur').estaAbierta())

print("\nHabitación 2:")
print("Norte es puerta:", hab2.obtenerElementoOr('norte').esPuerta())
print("Puerta está abierta:", hab2.obtenerElementoOr('norte').estaAbierta())