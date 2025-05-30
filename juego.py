from copy import deepcopy
from abc import ABC, abstractmethod
import random

# Patrón Singleton para las orientaciones
class Orientacion(ABC):
    @abstractmethod
    def poner_en_orientacion(self, contenedor, elemento_mapa):
        pass

    @abstractmethod
    def obtener_elemento_or(self, forma):
        pass

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Norte, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Cuadrado):
            contenedor.forma.norte = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Cuadrado):
            return forma.norte
        return None

class Sur(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sur, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Cuadrado):
            contenedor.forma.sur = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Cuadrado):
            return forma.sur
        return None

class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Este, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Cuadrado):
            contenedor.forma.este = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Cuadrado):
            return forma.este
        return None

class Oeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Oeste, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Cuadrado):
            contenedor.forma.oeste = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Cuadrado):
            return forma.oeste
        return None

class Noreste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Noreste, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Rombo):
            contenedor.forma.noreste = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Rombo):
            return forma.noreste
        return None

class Noroeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Noroeste, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Rombo):
            contenedor.forma.noroeste = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Rombo):
            return forma.noroeste
        return None

class Sureste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sureste, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Rombo):
            contenedor.forma.sureste = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Rombo):
            return forma.sureste
        return None

class Suroeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Suroeste, cls).__new__(cls)
        return cls._instance

    def poner_en_orientacion(self, contenedor, elemento_mapa):
        if isinstance(contenedor.forma, Rombo):
            contenedor.forma.suroeste = elemento_mapa

    def obtener_elemento_or(self, forma):
        if isinstance(forma, Rombo):
            return forma.suroeste
        return None

# Clase Forma (Patrón Bridge)
class Forma(ABC):
    def __init__(self):
        self.orientaciones = []

    def agregar_orientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def obtener_orientaciones(self):
        return self.orientaciones

    def poner_en_or_elemento(self, orientacion, elemento_mapa, contenedor):
        orientacion.poner_en_orientacion(contenedor, elemento_mapa)

    def obtener_elemento_or(self, orientacion):
        return orientacion.obtener_elemento_or(self)

    def obtener_orientacion_aleatoria(self):
        return random.choice(self.orientaciones)

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = [Norte(), Sur(), Este(), Oeste()]

class Rombo(Forma):
    def __init__(self):
        super().__init__()
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
        self.orientaciones = [Noreste(), Noroeste(), Sureste(), Suroeste()]

# Clase ElementoMapa y sus subclases
class ElementoMapa(ABC):
    def __init__(self, padre=None):
        self.padre = padre
        self.comandos = []

class Contenedor(ElementoMapa):
    def __init__(self, padre=None, forma=None, num=0):
        super().__init__(padre)
        self.hijos = []
        self.forma = forma
        self.num = num

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def agregar_orientacion(self, orientacion):
        self.forma.agregar_orientacion(orientacion)

    def obtener_orientaciones(self):
        return self.forma.obtener_orientaciones()

    def poner_en_or_elemento(self, orientacion, elemento_mapa):
        self.forma.poner_en_or_elemento(orientacion, elemento_mapa, self)

    def obtener_elemento_or(self, orientacion):
        return self.forma.obtener_elemento_or(orientacion)

    def obtener_orientacion_aleatoria(self):
        return self.forma.obtener_orientacion_aleatoria()

class Habitacion(Contenedor): pass
class Armario(Contenedor): pass
class Laberinto(Contenedor): pass

class Pared(ElementoMapa): pass
class ParedBomba(Pared):
    def __init__(self, padre=None, activa=False):
        super().__init__(padre)
        self.activa = activa

class Puerta(ElementoMapa):
    def __init__(self, lado1=None, lado2=None, estado=None):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.estado = estado

class EstadoPuerta(ABC): pass
class Abierta(EstadoPuerta): pass
class Cerrada(EstadoPuerta): pass

class Hoja(ElementoMapa): pass
class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

class Bomba(Decorator):
    def __init__(self, em, activa=False):
        super().__init__(em)
        self.activa = activa

class Tunel(Hoja):
    def __init__(self, laberinto=None):
        super().__init__()
        self.laberinto = laberinto

    def entrar(self, juego):
        self.laberinto = deepcopy(juego.prototipo)

# Clase Comando y sus subclases
class Comando(ABC):
    def __init__(self, receptor):
        self.receptor = receptor

    @abstractmethod
    def ejecutar(self):
        pass

class Entrar(Comando):
    def ejecutar(self):
        print(f"Entrando a {self.receptor}")

class Activar(Comando):
    def ejecutar(self):
        print(f"Activando {self.receptor}")

class Abrir(Comando):
    def ejecutar(self):
        print(f"Abriendo {self.receptor}")

class Cerrar(Comando):
    def ejecutar(self):
        print(f"Cerrando {self.receptor}")

# Clase Ente y sus subclases
class Ente(ABC):
    def __init__(self, poder, posicion, vidas, juego, estado_ente):
        self.poder = poder
        self.posicion = posicion
        self.vidas = vidas
        self.juego = juego
        self.estado_ente = estado_ente

class EstadoEnte(ABC): pass
class Vivo(EstadoEnte): pass
class Muerto(EstadoEnte): pass

class Bicho(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, modo):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.modo = modo

class Personaje(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, nombre):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.nombre = nombre

class Modo(ABC): pass
class Agresivo(Modo): pass
class Perezoso(Modo): pass

# Clase Juego
class Juego:
    def __init__(self, laberinto, bichos, person, prototipo):
        self.laberinto = laberinto
        self.bichos = bichos
        self.hilos = []
        self.person = person
        self.prototipo = prototipo

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un laberinto y su prototipo
    forma_cuadrado = Cuadrado()
    laberinto = Laberinto(forma=forma_cuadrado, num=1)
    prototipo = deepcopy(laberinto)

    # Crear habitaciones y puertas
    habitacion1 = Habitacion(forma=forma_cuadrado, num=1)
    habitacion2 = Habitacion(forma=forma_cuadrado, num=2)
    puerta = Puerta(lado1=habitacion1, lado2=habitacion2, estado=Cerrada())

    # Agregar elementos al laberinto
    laberinto.agregar_hijo(habitacion1)
    laberinto.agregar_hijo(habitacion2)
    laberinto.agregar_hijo(puerta)

    # Crear un personaje y bichos
    personaje = Personaje(poder=10, posicion=habitacion1, vidas=3, juego=None, estado_ente=Vivo(), nombre="Heroe")
    bicho = Bicho(poder=5, posicion=habitacion2, vidas=1, juego=None, estado_ente=Vivo(), modo=Agresivo())

    # Crear el juego
    juego = Juego(laberinto=laberinto, bichos=[bicho], person=personaje, prototipo=prototipo)
    personaje.juego = juego
    bicho.juego = juego

    # Ejecutar comandos
    comando_entrar = Entrar(receptor=habitacion1)
    comando_entrar.ejecutar()

    comando_abrir = Abrir(receptor=puerta)
    comando_abrir.ejecutar()

    # Probar los nuevos métodos
    nueva_orientacion = Norte()
    laberinto.poner_en_or_elemento(nueva_orientacion, puerta)
    elemento = laberinto.obtener_elemento_or(nueva_orientacion)
    print("Elemento en orientación Norte:", elemento)

    orientacion_aleatoria = laberinto.obtener_orientacion_aleatoria()
    print("Orientación aleatoria:", type(orientacion_aleatoria).__name__)