import json
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

    @abstractmethod
    def entrar(self, ente):
        pass

    def agregarComando(self, comando):
        self.comandos.append(comando)

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
    
    def entrar(self, ente):
        print(f"{ente} ha entrado en el contenedor {self.num}.")
        ente.posicion = self
        ente.buscarTunel()

class Habitacion(Contenedor): pass
class Armario(Contenedor): pass
class Laberinto(Contenedor):
    def obtenerHabitacion(self, num):
        for hijo in self.hijos:
            if isinstance(hijo, Habitacion) and hijo.num == num:
                return hijo
        return None

    def entrar(self, ente):
        habitacion = self.obtenerHabitacion(1)
        if habitacion:
            habitacion.entrar(ente)
        else:
            print("No se encontró la habitación número 1.")

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

    def entrar(self, ente):
        if self.laberinto is None:
            if isinstance(ente, Personaje):
                self.laberinto = deepcopy(ente.juego.prototipo)
                print(f"{ente} ha creado un nuevo laberinto.")
            else:
                print("Solo un personaje puede crear un nuevo laberinto.")
                return

        self.laberinto.entrar(ente)

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
    
    def buscarTunel(self):
        pass

class EstadoEnte(ABC): pass
class Vivo(EstadoEnte): pass
class Muerto(EstadoEnte): pass

class Bicho(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, modo):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.modo = modo

    def buscarTunel(self):
        self.modo.buscarTunelBicho(self)
    
    def __str__(self):
        return f"unBicho-{str(self.modo)}"

class Personaje(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, nombre):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.nombre = nombre

class Modo(ABC):
    def __str__(self):
        return self.__class__.__name__
    
    def buscarTunelBicho(self, bicho):
        pass

class Agresivo(Modo):
    def buscarTunelBicho(self, bicho):
        if bicho.posicion:
            for hijo in bicho.posicion.hijos:
                if isinstance(hijo, Tunel):
                    if hijo.laberinto:
                        print(f"{bicho} ha encontrado un túnel y está entrando.")
                        hijo.entrar(bicho)
                    else:
                        print(f"{bicho} ha encontrado un túnel, pero no tiene un laberinto creado.")
                    return
class Perezoso(Modo): pass

# Clase Juego
class Juego:
    def __init__(self, laberinto, bichos, person, prototipo):
        self.laberinto = laberinto
        self.bichos = bichos
        self.hilos = []
        self.person = person
        self.prototipo = prototipo

    def agregarBicho(self, bicho):
        self.bichos.append(bicho)
        bicho.juego = self

# Clase Creator
class Creator:
    def fabricarBomba(self, em, activa=False):
        return Bomba(em, activa)

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarJuego(self, laberinto, bichos, personaje, prototipo):
        return Juego(laberinto, bichos, personaje, prototipo)

    def fabricarLaberinto(self, forma=None, num=0):
        return Laberinto(forma=forma, num=num)

    def fabricarPared(self, padre=None):
        return Pared(padre)

    def fabricarPuerta(self, lado1=None, lado2=None, estado=None):
        return Puerta(lado1, lado2, estado)

    def fabricarHabitacion(self, num):
        habitacion = Habitacion(forma=Cuadrado(), num=num)
        habitacion.agregar_orientacion(self.fabricarNorte())
        habitacion.agregar_orientacion(self.fabricarSur())
        habitacion.agregar_orientacion(self.fabricarEste())
        habitacion.agregar_orientacion(self.fabricarOeste())

        habitacion.poner_en_or_elemento(self.fabricarNorte(), self.fabricarPared())
        habitacion.poner_en_or_elemento(self.fabricarSur(), self.fabricarPared())
        habitacion.poner_en_or_elemento(self.fabricarEste(), self.fabricarPared())
        habitacion.poner_en_or_elemento(self.fabricarOeste(), self.fabricarPared())

        return habitacion

    def fabricarBichoAgresivo(self, posicion, juego, estado_ente):
        return Bicho(poder=5, posicion=posicion, vidas=5, juego=juego, estado_ente=estado_ente, modo=Agresivo())

    def fabricarBichoPerezoso(self, posicion, juego, estado_ente):
        return Bicho(poder=1, posicion=posicion, vidas=1, juego=juego, estado_ente=estado_ente, modo=Perezoso())

    def cambiarModoAgresivo(self, bicho):
        bicho.modo = Agresivo()
        bicho.poder = 5
        bicho.vidas = 5

# Subclase CreatorB
class CreatorB(Creator):
    def fabricarPared(self, padre=None):
        return ParedBomba(padre, activa=False)

class LaberintoBuilder:
    def __init__(self):
        self.juego = None
        self.laberinto = None

    def obtenerJuego(self):
        return self.juego

    def fabricarLaberinto(self):
        self.laberinto = Laberinto(forma=Cuadrado())

    def fabricarArmarioEn(self, num, contenedor):
        armario = Armario(forma=Cuadrado(), num=num)
        for orientacion in armario.obtener_orientaciones():
            armario.poner_en_or_elemento(orientacion, Pared(), armario)
        contenedor.agregar_hijo(armario)
        return armario

    def fabricarBichoAgresivo(self, habitacion, estado_ente):
        bicho = Bicho(poder=5, posicion=habitacion, vidas=5, juego=self.juego, estado_ente=estado_ente, modo=Agresivo())
        return bicho
    
    def fabricarBichoPerezoso(self, habitacion):
        bicho = Bicho(poder=1, posicion=habitacion, vidas=1, juego=self.juego, estado_ente=Vivo(), modo=Perezoso())
        return bicho

    def fabricarBichoModoPosicion(self, modo, num):
        if modo == "agresivo":
            bicho = self.fabricarBichoAgresivo(self.juego.laberinto.obtenerHabitacion(num))
        elif modo == "perezoso":
            bicho = self.fabricarBichoPerezoso(self.juego.laberinto.obtenerHabitacion(num))
        else:
            raise ValueError("Modo no reconocido.")

        if bicho:
            self.juego.agregarBicho(bicho)
            bicho.posicion.entrar(bicho)

    def fabricarBombaEn(self, contenedor):
        bomba = Bomba()
        contenedor.agregar_hijo(bomba)
        return bomba

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarForma(self):
        forma = Cuadrado()
        forma.agregar_orientacion(self.fabricarNorte())
        forma.agregar_orientacion(self.fabricarSur())
        forma.agregar_orientacion(self.fabricarEste())
        forma.agregar_orientacion(self.fabricarOeste())
        return forma
    
    def fabricarHabitacion(self, num):
        habitacion = Habitacion(forma=self.fabricarForma(), num=num)
        for orientacion in habitacion.obtener_orientaciones():
            habitacion.poner_en_or_elemento(orientacion, Pared(), habitacion)
        self.laberinto.agregar_hijo(habitacion)
        return habitacion
    
    def fabricarJuego(self):
        self.juego = Juego(laberinto=None, bichos=[], personaje=None, prototipo=None)
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = deepcopy(self.juego.prototipo)

    def fabricarPuertaL1Or1L2Or2(self, num1, or1, num2, or2):
        habitacion1 = self.laberinto.obtenerHabitacion(num1)
        habitacion2 = self.laberinto.obtenerHabitacion(num2)

        puerta = Puerta(lado1=habitacion1, lado2=habitacion2)
        puerta.agregarComando(Abrir(receptor=puerta))

        orientacion1 = self.obtenerOrientacion(or1)
        orientacion2 = self.obtenerOrientacion(or2)

        habitacion1.poner_en_or_elemento(orientacion1, puerta, habitacion1)
        habitacion2.poner_en_or_elemento(orientacion2, puerta, habitacion2)

    def obtenerOrientacion(self, or_str):
        if or_str == "norte":
            return self.fabricarNorte()
        elif or_str == "sur":
            return self.fabricarSur()
        elif or_str == "este":
            return self.fabricarEste()
        elif or_str == "oeste":
            return self.fabricarOeste()
        else:
            raise ValueError("Orientación no reconocida.")

    def fabricarTunelEn(self, contenedor):
        tunel = Tunel()
        tunel.agregarComando(Entrar(receptor=tunel))
        contenedor.agregar_hijo(tunel)
        return tunel

class LaberintoBuilderRombo(LaberintoBuilder):
    def construirLaberinto(self):
        self.laberinto = Laberinto(forma=Rombo())

    def fabricarArmarioEn(self, num, contenedor):
        armario = Armario(forma=Rombo(), num=num)
        for orientacion in armario.obtener_orientaciones():
            armario.poner_en_or_elemento(orientacion, Pared(), armario)
        contenedor.agregar_hijo(armario)
        return armario

class Director:
    def __init__(self):
        self.builder = None
        self.dict = {}

    def leerArchivo(self, archivo_json):
        with open(archivo_json, 'r') as archivo:
            self.dict = json.load(archivo)

    def iniBuilder(self):
        forma = self.dict.get("forma", "cuadrado")
        if forma == "cuadrado":
            self.builder = LaberintoBuilder()
        elif forma == "rombo":
            self.builder = LaberintoBuilderRombo()
        else:
            raise ValueError("Forma no reconocida en el archivo JSON.")


# ---------------------Ejemplo de uso---------------------
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