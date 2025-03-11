# Archivo que contiene el juego del laberinto
from abc import ABC, abstractmethod
from random import *

class ElementoMapa(ABC): #COMPLETA HASTA 11/03/2025
    """Clase base para los elementos del laberinto."""
    def __init__(self, padre=None):
        self.padre = padre

    def es_pared(self):
        return False
    
    def es_puerta(self):
        return False
    
    def es_habitacion(self):
        return False
    
    @abstractmethod
    def entrar(self, alguien):
        pass

class Contenedor(ElementoMapa): #COMPLETA HASTA 11/03/2025
    def __init__(self, padre=None):
        super().__init__(padre)
        self.hijos = []
        self.orientaciones = []
    
    def agregar_hijo(self, unEM):
        self.hijos.append(unEM)
        unEM.padre = self

    def agregar_orientacion(self, unaOr): 
        self.orientaciones.append(unaOr)
    
    def eliminar_hijo(self, unEM):
        if unEM in self.hijos:
            self.hijos.remove(unEM)
            unEM.padre = None
        else:
            print("No existe el objeto")

    def obtener_elemento_or(self, unaOr):
        return unaOr.obtener_elemento_or_en(self)
    
    def obtener_orientacion(self):
        ind = randint(1, len(self.orientaciones))
        return self.orientaciones[ind]
    
    def poner_en_or_elemento(self, unaOr, unEM):
        unaOr.poner_elemento_en(unEM, self)

    # def recorrer(self, unBloque):
    #     unBloque(self)
    #     for hijo in self.hijos:
    #         hijo.recorrer(unBloque)
        
    #     for ori in self.orientaciones:
    #         ori.recorrer_contenedor(unBloque, self)

class Habitacion(Contenedor): #COMPLETA HASTA 11/03/2025
    """Representa una habitación en el laberinto con elementos en las 4 direcciones."""
    def __init__(self, numero, padre=None):
        super().__init__(padre)
        self.num = numero
        self.elementos = {
            'norte': None,
            'sur': None,
            'este': None,
            'oeste': None
        }
    
    def entrar(self, alguien):
        print(f"{alguien} está en {self}")
        alguien.posicion = self

    def es_habitacion(self):
        return True
    
    def ir_al_norte(self, alguien):
        self.elementos["norte"].entrar(alguien)

    def ir_al_sur(self, alguien):
        self.elementos["sur"].entrar(alguien)

    def ir_al_este(self, alguien):
        self.elementos["este"].entrar(alguien)

    def ir_al_oeste(self, alguien):
        self.elementos["oeste"].entrar(alguien)
    
    def __repr__(self):
         return f"Hab {self.num}"
    
class Laberinto(Contenedor): #COMPLETA HASTA 11/03/2025 (modificar abrir_puertas y cerrar_puertas)
    def __init__(self, padre=None):
        super().__init__(padre)

    def abrir_puertas(self):
        for habitacion in self.hijos:
            for orientacion, elemento in habitacion.orientaciones.items():
                if isinstance(elemento, Puerta): #elemento.es_puerta
                    elemento.abierta = True #elemento.abrir

    def agregar_habitacion(self, unaHabitacion):
        self.agregar_hijo(unaHabitacion)
    
    def cerrar_puertas(self):
        for habitacion in self.hijos:
            for orientacion, elemento in habitacion.orientaciones.items():
                if isinstance(elemento, Puerta): #elemento.es_puerta
                    elemento.abierta = False #elemento.cerrar
    
    def eliminar_habitacion(self, habitacion):
        self.eliminar_hijo(habitacion)

    def obtener_habitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None

    def entrar(self, alguien):
        hab1 = self.obtener_habitacion(1)
        hab1.entrar(alguien)

    def __repr__(self):
         return f"Laberinto"
    
class Hoja(ElementoMapa): #COMPLETA HASTA 11/03/2025
    def __init__(self, padre=None):
        super().__init__(padre)

class Decorator(Hoja): #COMPLETA HASTA 11/03/2025
    def __init__(self, padre=None):
        super().__init__(padre)
        self.em = None

class Bomba(Decorator): #COMPLETA HASTA 11/03/2025
    def __init__(self, padre=None):
        super().__init__(padre)
        self.activa = False

    def entrar(self, alguien):
        if (self.activa):
            print(f"{alguien} ha chocado con una bomba")
        else:
            self.em.entrar(alguien)

class Pared(ElementoMapa):
    """Representa una pared en el laberinto."""
    def entrar(self):
        print("Te has chocado con una pared")

    def esPared(self):
        return True
    
class ParedBomba(Pared):
    def __init__(self):
        self.activa = False

    def getActiva(self):
        return self.activa
    
    def setActiva(self, activa):
        self.activa = activa

    def entrar(self):
        print("Te has chocado con una pared bomba")

class Puerta(ElementoMapa):
    """Representa una puerta que conecta habitaciones."""
    def __init__(self):
        self.abierta = False

    def getAbierta(self):
        return self.abierta
    
    def setAbierta(self, abierta):
        self.abierta = abierta

    def getLado1(self):
        return self.lado1
    
    def setLado1(self, lado):
        self.lado1 = lado

    def getLado2(self):
        return self.lado2
    
    def setLado2(self, lado):
        self.lado2 = lado

    def esPuerta(self):
        return True
    
    def entrar(self):
        if(self.abierta == True):
            print("La puerta está abierta")
        else:
            print("Te has chocado con una puerta")

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

#PRUEBA DEL JUEGO (NO FUNCIONA - NO ACTUALIZADO)
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