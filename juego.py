# %%
import json
from copy import deepcopy
from abc import ABC, abstractmethod
import random
import threading
import time

# Patrón Singleton para las orientaciones
class Orientacion(ABC):
    @abstractmethod
    def poner_en_orientacion(self, contenedor, elemento_mapa):
        pass

    @abstractmethod
    def obtener_elemento_or(self, forma):
        pass

    @abstractmethod
    def caminar(self, ente):
        pass

    def iterar_contenedor(self, funcion, forma):
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
    
    def caminar(self, ente):
        if isinstance(ente.posicion.forma, Cuadrado):
            ente.posicion.forma.irAlNorte(ente)

    def iterar_contenedor(self, funcion, forma):
        if forma.norte:
            forma.norte.iterar(funcion)

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
    
    def caminar(self, ente):
        if isinstance(ente.posicion.forma, Cuadrado):
            ente.posicion.forma.irAlSur(ente)

    def iterar_contenedor(self, funcion, forma):
        if forma.sur:
            forma.sur.iterar(funcion)

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
    
    def caminar(self, ente):
        if isinstance(ente.posicion.forma, Cuadrado):
            ente.posicion.forma.irAlEste(ente)

    def iterar_contenedor(self, funcion, forma):
        if forma.este:
            forma.este.iterar(funcion)

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
    
    def caminar(self, ente):
        if isinstance(ente.posicion.forma, Cuadrado):
            ente.posicion.forma.irAlOeste(ente)

    def iterar_contenedor(self, funcion, forma):
        if forma.oeste:
            forma.oeste.iterar(funcion)

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
    
    def irAlNorte(self, ente):
        pass

    def irAlSur(self, ente):
        pass

    def irAlEste(self, ente):
        pass

    def irAlOeste(self, ente):
        pass

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = [Norte(), Sur(), Este(), Oeste()]

    def irAlNorte(self, ente):
        if self.norte:
            self.norte.entrar(ente)

    def irAlSur(self, ente):
        if self.sur:
            self.sur.entrar(ente)

    def irAlEste(self, ente):
        if self.este:
            self.este.entrar(ente)

    def irAlOeste(self, ente):
        if self.oeste:
            self.oeste.entrar(ente)

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

    def entrar(self, ente):
        pass

    def agregarComando(self, comando):
        self.comandos.append(comando)

    def aceptar(self, visitor):
        pass

    def iterar(self, funcion):
        funcion(self)

    def eliminarComando(self, comando):
        if comando in self.comandos:
            self.comandos.remove(comando)

    def obtenerComandos(self):
        return self.comandos

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
        print(f"{ente} ha entrado en el contenedor {self}.")
        ente.posicion = self
        ente.buscarTunel()

    def irAlNorte(self, ente):
        self.forma.irAlNorte(ente)

    def irAlSur(self, ente):
        self.forma.irAlSur(ente)

    def irAlEste(self, ente):
        self.forma.irAlEste(ente)

    def irAlOeste(self, ente):
        self.forma.irAlOeste(ente)

    def aceptar(self, visitor):
        for hijo in self.hijos:
            hijo.aceptar(visitor)

    def eliminarHijo(self, hijo):
        if hijo in self.hijos:
            self.hijos.remove(hijo)

    def iterar(self, funcion):
        funcion(self)
        for hijo in self.hijos:
            hijo.iterar(funcion)
        for orientacion in self.obtener_orientaciones():
            orientacion.iterar_contenedor(funcion, self.forma)

class Habitacion(Contenedor):
    def aceptar(self, visitor):
        visitor.visitarHabitacion(self)
        super().aceptar(visitor)

    def __str__(self):
        return f"Habitacion {self.num}"
    
    def entrar(self, ente):
        print(f"{ente} ha entrado en el contenedor {self}.")
        ente.posicion = self
        # Verificar si la habitación contiene una bomba
        for hijo in self.hijos:
            if isinstance(hijo, Bomba):
                print(f"¡Cuidado! {ente} ha entrado en una habitación con una bomba.")
                if hijo.activa:
                    hijo.entrar(ente)
                break
        ente.buscarTunel()

class Armario(Contenedor): 
    def aceptar(self, visitor):
        visitor.visitarArmario(self)
        super().aceptar(visitor)

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

    def aceptar(self, visitor):
        for hijo in self.hijos:
            hijo.aceptar(visitor)

    def agregarHabitacion(self, habitacion):
        self.agregar_hijo(habitacion)

    def iterar(self, funcion):
        funcion(self)
        for hijo in self.hijos:
            hijo.iterar(funcion)
    
    def abrirPuertas(self):
        def abrir_puerta(obj):
            if isinstance(obj, Puerta):
                obj.abrir()
        self.iterar(abrir_puerta)

class Pared(ElementoMapa):
    def entrar(self, ente):
        print(f"{ente} ha chocado con una pared.")

    def aceptar(self, visitor):
        visitor.visitarPared(self)

class ParedBomba(Pared):
    def __init__(self, padre=None, activa=False):
        super().__init__(padre)
        self.activa = activa

class Puerta(ElementoMapa):
    def __init__(self, lado1=None, lado2=None, estado=None):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.estado = estado if estado else Cerrada()

    def __str__(self):
        return f"Puerta {self.lado1.num}-{self.lado2.num}"

    def aceptar(self, visitor):
        visitor.visitarPuerta(self)

    def abrir(self):
        self.estado.abrir(self)

    def cerrar(self):
        self.estado.cerrar(self)

    def entrar(self, ente):
        self.estado.entrarPuerta(self, ente)

    def puedeEntrar(self, ente):
        if ente.posicion == self.lado1:
            self.lado2.entrar(ente)
        else:
            self.lado1.entrar(ente)

class EstadoPuerta(ABC):
    @abstractmethod
    def abrir(self, puerta):
        pass

    @abstractmethod
    def cerrar(self, puerta):
        pass

    @abstractmethod
    def entrarPuerta(self, puerta, ente):
        pass

class Abierta(EstadoPuerta):
    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        print(f"La {puerta} está cerrada.")
        puerta.estado = Cerrada()

    def entrarPuerta(self, puerta, ente):
        puerta.puedeEntrar(ente)

class Cerrada(EstadoPuerta):
    def abrir(self, puerta):
        print(f"La {puerta} está abierta.")
        puerta.estado = Abierta()

    def cerrar(self, puerta):
        pass

    def entrarPuerta(self, puerta, ente):
        print(f"{ente} se ha chocado con {puerta}.")

class Hoja(ElementoMapa): pass
class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

class Bomba(Decorator):
    def __init__(self, em=None, activa=False):
        super().__init__(em)
        self.activa = activa

    def activar(self):
        self.activa = True
        print("La bomba está activa.")

    def __str__(self):
        return "bomba"

    def aceptar(self, visitor):
        visitor.visitarBomba(self)

    def entrar(self, ente):
        if self.activa and isinstance(ente, Personaje):
            if isinstance(ente.clase, Tanque):
                print(f"{ente} ha chocado con una bomba, pero es un tanque y no le afecta.")
            else:
                ente.vidas -= 5
                print(f"{ente} ha chocado con una bomba. Vida = {ente.vidas}")
            self.activa = False

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

    def aceptar(self, visitor):
        visitor.visitarTunel(self)
    
    def __str__(self):
        return self.__class__.__name__

# Clase Comando y sus subclases
class Comando(ABC):
    def __init__(self, receptor):
        self.receptor = receptor

    @abstractmethod
    def ejecutar(self, ente):
        pass

    def __str__(self):
        pass
        

class Abrir(Comando):
    def ejecutar(self, ente):
        self.receptor.abrir()

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"
    
class Cerrar(Comando):
    def ejecutar(self, ente):
        self.receptor.cerrar()

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"

class Entrar(Comando):
    def ejecutar(self, ente):
        self.receptor.entrar(ente)

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"

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

    def atacar(self):
        self.estado_ente.atacar(self)

    def puedeAtacar(self):
        pass

    def esAtacadoPor(self, atacante):
        self.vidas -= atacante.poder
        print(f"{self} ha sido atacado por {atacante}. Vida restante: {self.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

    def heMuerto(self):
        self.estado_ente = Muerto()
        self.avisar()

    def avisar(self):
        pass

class EstadoEnte(ABC):
    @abstractmethod
    def actuar(self, bicho):
        pass

    @abstractmethod
    def atacar(self, ente):
        pass

class Vivo(EstadoEnte):
    def actuar(self, bicho):
        bicho.puedeActuar()

    def atacar(self, ente):
        ente.puedeAtacar()

class Muerto(EstadoEnte):
    def actuar(self, bicho):
        pass

    def atacar(self, ente):
        pass

class Bicho(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, modo):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.modo = modo

    def buscarTunel(self):
        self.modo.buscarTunelBicho(self)
    
    def __str__(self):
        return f"unBicho-{str(self.modo)}"
    
    def obtenerOrientacion(self):
        return self.posicion.obtener_orientacion_aleatoria()
    
    def puedeAtacar(self):
        self.juego.buscarPersonaje(self)

    def puedeActuar(self):
        self.modo.actuar(self)

    def actuar(self):
        self.estado_ente.actuar(self)

    def avisar(self):
        self.juego.terminarBicho(self)

    def esRobadoPor(self, personaje, arma):
        self.vidas -= personaje.poder
        if isinstance(arma.modelo, RobaBicho):
            personaje.vidas += arma.vida
        print(f"{self} ha sido atacado por {personaje}. Vida restante: {self.vidas}")
        print(f"Vida de {personaje} total: {personaje.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

class Personaje(Ente):
    def __init__(self, poder, posicion, vidas, juego, estado_ente, nombre, clase):
        super().__init__(poder, posicion, vidas, juego, estado_ente)
        self.nombre = nombre
        self.inventario = Inventario()
        self.clase = clase

    def __str__(self):
        return f"{self.nombre}-{str(self.clase)}"
    
    def robarVida(self, arma):
        self.juego.buscarBichoRobar(self, arma)

    def puedeAtacar(self):
        self.juego.buscarBicho(self)

    def avisar(self):
        self.juego.muerePersonaje()

    def obtenerComandos(self):
        comandos = set()
        def obtener_comandos(obj):
            comandos.update(obj.obtenerComandos())
        self.posicion.iterar(obtener_comandos)
        self.inventario.iterar(obtener_comandos)

        return list(comandos)
    
    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def irAlSur(self):
        self.posicion.irAlSur(self)

    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlOeste(self):
        self.posicion.irAlOeste(self)

    def curarse(self):
        if isinstance(self.clase, Curandero):
            self.clase.habilidad_especial(self)

class Modo(ABC):
    def __str__(self):
        return self.__class__.__name__
    
    def buscarTunelBicho(self, bicho):
        pass

    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
        self.atacar(bicho)

    @abstractmethod
    def dormir(self, bicho):
        pass

    @abstractmethod
    def caminar(self, bicho):
        pass

    def atacar(self, bicho):
        bicho.atacar()

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
                
    def dormir(self, bicho):
        print(f"{bicho} está durmiendo.")
        time.sleep(1)

    def caminar(self, bicho):
        orientacion = bicho.obtenerOrientacion()
        orientacion.caminar(bicho)

class Perezoso(Modo):
    def dormir(self, bicho):
        print(f"{bicho} está durmiendo.")
        time.sleep(3)

    def caminar(self, bicho):
        orientacion = bicho.obtenerOrientacion()
        orientacion.caminar(bicho)

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

    def eliminarBicho(self, bicho):
        if bicho in self.bichos:
            self.bichos.remove(bicho)

    def agregarPersonaje(self, nombre, clase):
        if clase == "Tanque":
            personaje = Personaje(poder=6, posicion=None, vidas=70, juego=self, estado_ente=Vivo(), nombre=nombre, clase=Tanque())
        elif clase == "Asesino":
            personaje = Personaje(poder=15, posicion=None, vidas=40, juego=self, estado_ente=Vivo(), nombre=nombre, clase=Asesino())
        elif clase == "Curandero":
            personaje = Personaje(poder=3, posicion=None, vidas=30, juego=self, estado_ente=Vivo(), nombre=nombre, clase=Curandero())
        else:
            raise ValueError("Clase de personaje no reconocida.")
        self.person = personaje
        personaje.juego = self
        self.laberinto.entrar(personaje)

    def ganaPersonaje(self):
        print("¡El personaje ha ganado! El juego ha terminado.")

    def muerePersonaje(self):
        print("¡Fin de la partida! Los bichos han ganado.")
        self.terminarBichos()

    def abrirPuertas(self):
        self.laberinto.abrirPuertas()

    def cerrarPuertas(self):
        self.laberinto.cerrarPuertas()

    def lanzarBicho(self, bicho):
        def ciclo_vida_bicho():
            while isinstance(bicho.estado_ente, Vivo):
                bicho.actuar()

        hilo = threading.Thread(target=ciclo_vida_bicho)
        hilo.start()
        self.hilos.append(hilo)

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBicho(self, bicho):
        bicho.estado_ente = Muerto()
        bicho.vidas = 0
        print(f"{bicho} ha muerto.")
        if isinstance(self.person.estado_ente, Vivo) and all(isinstance(b.estado_ente, Muerto) for b in self.bichos):
            self.ganaPersonaje()

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def buscarPersonaje(self, bicho):
        if bicho.posicion == self.person.posicion:
            self.person.esAtacadoPor(bicho)

    def buscarBicho(self, personaje):
        for bicho in self.bichos:
            if bicho.posicion == personaje.posicion and isinstance(bicho.estado_ente, Vivo):
                bicho.esAtacadoPor(personaje)

    def buscarBichoRobar(self, personaje, arma):
        for bicho in self.bichos:
            if bicho.posicion == personaje.posicion and isinstance(bicho.estado_ente, Vivo):
                bicho.esRobadoPor(personaje, arma)

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
        return Bicho(poder=5, posicion=posicion, vidas=20, juego=juego, estado_ente=estado_ente, modo=Agresivo())

    def fabricarBichoPerezoso(self, posicion, juego, estado_ente):
        return Bicho(poder=1, posicion=posicion, vidas=10, juego=juego, estado_ente=estado_ente, modo=Perezoso())

    def cambiarModoAgresivo(self, bicho):
        bicho.modo = Agresivo()
        bicho.poder = 5
        bicho.vidas = 20

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
            armario.poner_en_or_elemento(orientacion, Pared())
        contenedor.agregar_hijo(armario)
        return armario

    def fabricarBichoAgresivo(self, habitacion):
        bicho = Bicho(poder=5, posicion=habitacion, vidas=20, juego=self.juego, estado_ente=Vivo(), modo=Agresivo())
        return bicho
    
    def fabricarBichoPerezoso(self, habitacion):
        bicho = Bicho(poder=1, posicion=habitacion, vidas=10, juego=self.juego, estado_ente=Vivo(), modo=Perezoso())
        return bicho

    def fabricarBichoModoPosicion(self, modo, num):
        if modo == "Agresivo":
            bicho = self.fabricarBichoAgresivo(self.juego.laberinto.obtenerHabitacion(num))
        elif modo == "Perezoso":
            bicho = self.fabricarBichoPerezoso(self.juego.laberinto.obtenerHabitacion(num))
        else:
            raise ValueError("Modo no reconocido.")

        if bicho:
            self.juego.agregarBicho(bicho)
            bicho.posicion.entrar(bicho)

    def fabricarArmaEn(self, contenedor, nombre, modelo):
        if modelo == "robabicho":
            arma = self.fabricarArmaRobaBicho(nombre, modelo)
            contenedor.agregar_hijo(arma)
        elif modelo == "chupavida":
            arma = self.fabricarArmaChupaVida(nombre, modelo)
            contenedor.agregar_hijo(arma)

    def fabricarArmaRobaBicho(self, nombre, modelo):
        arma = Arma(nombre=nombre, daño=4, vida=4, modelo=RobaBicho())
        arma.agregarComando(Recoger(receptor=arma))
        return arma
    
    def fabricarArmaChupaVida(self, nombre, modelo):
        arma = Arma(nombre=nombre, daño=8, vida=2, modelo=ChupaVida())
        arma.agregarComando(Recoger(receptor=arma))
        return arma
    
    def fabricarPocionEn(self, contenedor, vida, nombre):
        pocion = Pocion(nombre=nombre, vidaRestaurada=vida)
        pocion.agregarComando(Recoger(receptor=pocion))
        contenedor.agregar_hijo(pocion)
        return pocion
    
    def fabricarLlaveEn(self, contenedor, nombre):
        llave = Llave(nombre=nombre)
        llave.agregarComando(Recoger(receptor=llave))
        contenedor.agregar_hijo(llave)
        return llave

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
            habitacion.poner_en_or_elemento(orientacion, Pared())
        self.laberinto.agregar_hijo(habitacion)
        return habitacion
    
    def fabricarJuego(self):
        self.juego = Juego(laberinto=None, bichos=[], person=None, prototipo=None)
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = deepcopy(self.juego.prototipo)

    def fabricarPuertaL1Or1L2Or2(self, num1, or1, num2, or2):
        habitacion1 = self.laberinto.obtenerHabitacion(num1)
        habitacion2 = self.laberinto.obtenerHabitacion(num2)

        puerta = Puerta(lado1=habitacion1, lado2=habitacion2)
        puerta.agregarComando(Abrir(receptor=puerta))
        puerta.agregarComando(Cerrar(receptor=puerta))

        orientacion1 = self.obtenerOrientacion(or1)
        orientacion2 = self.obtenerOrientacion(or2)

        habitacion1.poner_en_or_elemento(orientacion1, puerta)
        habitacion2.poner_en_or_elemento(orientacion2, puerta)

    def fabricarPuertaConCandadoL1Or1L2Or2(self, num1, or1, num2, or2, nombre):
        habitacion1 = self.laberinto.obtenerHabitacion(num1)
        habitacion2 = self.laberinto.obtenerHabitacion(num2)

        puerta = Puerta(lado1=habitacion1, lado2=habitacion2)
        puerta_con_candado = Candado(puerta, nombre)
        puerta_con_candado.agregarComando(Desbloquear(receptor=puerta_con_candado))

        orientacion1 = self.obtenerOrientacion(or1)
        orientacion2 = self.obtenerOrientacion(or2)

        habitacion1.poner_en_or_elemento(orientacion1, puerta_con_candado)
        habitacion2.poner_en_or_elemento(orientacion2, puerta_con_candado)

    def obtenerOrientacion(self, or_str):
        if or_str == "Norte":
            return self.fabricarNorte()
        elif or_str == "Sur":
            return self.fabricarSur()
        elif or_str == "Este":
            return self.fabricarEste()
        elif or_str == "Oeste":
            return self.fabricarOeste()
        else:
            raise ValueError("Orientación no reconocida.")

    def fabricarTunelEn(self, contenedor):
        tunel = Tunel()
        tunel.agregarComando(Entrar(receptor=tunel))
        contenedor.agregar_hijo(tunel)
        return tunel

class LaberintoBuilderRombo(LaberintoBuilder):
    def fabricarLaberinto(self):
        self.laberinto = Laberinto(forma=Rombo())

    def fabricarArmarioEn(self, num, contenedor):
        armario = Armario(forma=Rombo(), num=num)
        for orientacion in armario.obtener_orientaciones():
            armario.poner_en_or_elemento(orientacion, Pared())
        contenedor.agregar_hijo(armario)
        return armario

    def fabricarNoreste(self):
        return Noreste()

    def fabricarNoroeste(self):
        return Noroeste()

    def fabricarSureste(self):
        return Sureste()

    def fabricarSuroeste(self):
        return Suroeste()

    def fabricarForma(self):
        forma = Rombo()
        forma.agregar_orientacion(self.fabricarNoreste())
        forma.agregar_orientacion(self.fabricarNoroeste())
        forma.agregar_orientacion(self.fabricarSureste())
        forma.agregar_orientacion(self.fabricarSuroeste())
        return forma

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
        
    def construirLaberinto(self):
        if self.builder:
            self.builder.fabricarLaberinto()
            self.fabricarHabitaciones()
            self.fabricarPuertas()
            self.fabricarJuego()
            self.fabricarBichos()

    def fabricarHabitaciones(self):
        for item in self.dict.get("laberinto", []):
            if item["tipo"] == "habitacion":
                habitacion = self.builder.fabricarHabitacion(item["num"])
                for hijo in item.get("hijos", []):
                    if hijo["tipo"] == "armario":
                        self.builder.fabricarArmarioEn(hijo["num"], habitacion)
                    elif hijo["tipo"] == "bomba":
                        self.builder.fabricarBombaEn(habitacion)
                    elif hijo["tipo"] == "tunel":
                        self.builder.fabricarTunelEn(habitacion)
                    elif hijo["tipo"] == "arma":
                        self.builder.fabricarArmaEn(habitacion, hijo["nombre"], hijo["modelo"])
                    elif hijo["tipo"] == "pocion":
                        self.builder.fabricarPocionEn(habitacion, hijo["vida"], hijo["nombre"])
                    elif hijo["tipo"] == "llave":
                        self.builder.fabricarLlaveEn(habitacion, hijo["nombre"])

    def fabricarPuertas(self):
        for puerta in self.dict.get("puertas", []):
            self.builder.fabricarPuertaL1Or1L2Or2(puerta[0], puerta[1], puerta[2], puerta[3])
        for puerta in self.dict.get("puerta_bloqueada", []):
            self.builder.fabricarPuertaConCandadoL1Or1L2Or2(puerta[0], puerta[1], puerta[2], puerta[3], puerta[4])

    def fabricarBichos(self):
        bichos = self.dict.get('bichos', [])
        for bicho_info in bichos:
            modo = bicho_info.get('modo')
            posicion = bicho_info.get('posicion')
            self.builder.fabricarBichoModoPosicion(modo, posicion)

    def obtenerJuego(self):
        return self.builder.obtenerJuego()
    
    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def procesar(self, archivo_json):
        self.leerArchivo(archivo_json)
        self.iniBuilder()
        self.construirLaberinto()

class Visitor(ABC):
    def visitarArmario(self, armario):
        pass

    def visitarBomba(self, bomba):
        pass

    def visitarHabitacion(self, habitacion):
        pass

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        pass

    def visitarTunel(self, tunel):
        pass

    def visitar_arma(self, arma):
        pass

    def visitar_llave(self, arma):
        pass

    def visitar_pocion(self, arma):
        pass

class VisitorActivarBombas(Visitor):
    def visitarBomba(self, bomba):
        bomba.activar()

#-----------------------------IMPLEMENTACIONES-----------------------------
# Clase Inventario
class Inventario:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def aceptar(self, visitor):
        for elemento in self.elementos:
            elemento.aceptar(visitor)

    def iterar(self, funcion):
        for elemento in self.elementos:
            elemento.iterar(funcion)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

# Clase ElementoRecogible
class ElementoRecogible(Hoja):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def aceptar(self, visitor):
        pass

    def recoger(self, personaje):
        pass

class Arma(ElementoRecogible):
    def __init__(self, nombre, daño, vida, modelo=None):
        super().__init__(nombre)
        self.daño = daño
        self.vida = vida
        self.modelo = modelo

    def __str__(self):
        return f"Arma-{str(self.modelo)}-{self.nombre}"

    def aceptar(self, visitor):
        visitor.visitar_arma(self)

    def recoger(self, personaje):
        self.comandos = [(Atacar(receptor=self))]
        personaje.inventario.agregar_elemento(self)
        print(f"{personaje} ha recogido el arma {self.nombre}. Daño: {self.daño}, Vida: {self.vida}")

    def atacar(self, personaje):
        self.modelo.atacar(personaje, self)

class Modelo(ABC):
    @abstractmethod
    def atacar(self, personaje, arma):
        pass

class RobaBicho(Modelo):
    def __str__(self):
        return self.__class__.__name__
    
    def atacar(self, personaje, arma):
        personaje.poder += arma.daño
        personaje.robarVida(arma)
        time.sleep(2)


class ChupaVida(Modelo):
    def __str__(self):
        return self.__class__.__name__
    
    def atacar(self, personaje, arma):
        personaje.poder += arma.daño
        personaje.vidas -= arma.vida
        print(f"{personaje} ha usado {arma.nombre}. Vida total del personaje: {personaje.vidas}")
        personaje.robarVida(arma)
        

class Pocion(ElementoRecogible):
    def __init__(self, nombre, vidaRestaurada):
        super().__init__(nombre)
        self.vida_restaurada = vidaRestaurada

    def __str__(self):
        return f"Pocion-{self.nombre}"
    
    def aceptar(self, visitor):
        visitor.visitar_pocion(self)

    def recoger(self, personaje):
        self.comandos = [(Usar(receptor=self))]
        personaje.inventario.agregar_elemento(self)
        print(f"{personaje} ha recogido la pocion {self.nombre}. Vida que proporciona: {self.vida_restaurada}")

    def usar(self, personaje):
        personaje.vidas += self.vida_restaurada
        self.comandos = []
        personaje.inventario.eliminar_elemento(self)
        print(f"{personaje} ha usado la poción {self.nombre}. Vida total del personaje: {personaje.vidas}")

class Llave(ElementoRecogible):
    def aceptar(self, visitor):
        visitor.visitar_llave(self)

    def __str__(self):
        return f"Llave-{self.nombre}"
    
    def recoger(self, personaje):
        self.comandos = []
        personaje.inventario.agregar_elemento(self)
        print(f"{personaje} ha recogido la llave {self.nombre}")

# Clase Visitor para visitar el inventario y listar elementos
class VisitorInventario(Visitor):
    def visitar_arma(self, arma):
        print(f"Arma en inventario: {arma.nombre}- Daño: {arma.daño}- Vida: {arma.vida}")

    def visitar_pocion(self, pocion):
        print(f"Poción en inventario: {pocion.nombre}- Vida Restaurada: {pocion.vida_restaurada}")

    def visitar_llave(self, llave):
        print(f"Llave en inventario: {llave.nombre}")

# Comandos para interactuar con el juego
class Recoger(Comando):
    def ejecutar(self, ente):
        self.receptor.recoger(ente)

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"
    
class Atacar(Comando):
    def ejecutar(self, ente):
        self.receptor.atacar(ente)

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"

class Usar(Comando):
    def ejecutar(self, ente):
        self.receptor.usar(ente)

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"
    
class Desbloquear(Comando):
    def ejecutar(self, ente):
        self.receptor.abrir(ente)

    def __str__(self):
        return f"{str(self.__class__.__name__)}-{self.receptor}"
    
# Clase Candado
class Candado(Decorator):
    def __init__(self, puerta, nombre):
        super().__init__(puerta)
        self.nombre = nombre

    def aceptar(self, visitor):
        visitor.visitarPuerta(self)

    def abrir(self, personaje):
        if isinstance(personaje, Personaje):
            tiene_llave = any(isinstance(elemento, Llave) and elemento.nombre == self.nombre for elemento in personaje.inventario.elementos)
            if tiene_llave:
                print(f"{personaje} ha abierto la puerta con candado usando una llave.")
                self.em.abrir()
                self.em.entrar(personaje)
                print(f"¡{personaje} ha entrado a la habitación del tesoro!")
                personaje.juego.ganaPersonaje()
            else:
                print(f"{personaje} no tiene la llave para abrir la puerta {self.em} con candado.")

    def entrar(self, ente):
        self.abrir(ente)

    def __str__(self):
        return f"Puerta con Candado {self.em.lado1.num}-{self.em.lado2.num}"

# Clase ClasePersonaje
class ClasePersonaje(ABC):
    @abstractmethod
    def habilidad_especial(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Tanque(ClasePersonaje):
    def habilidad_especial(self, personaje): pass
        # Los tanques resisten más daño de las bombas
        #print(f"{personaje.nombre} es un Tanque y resiste el daño de las bombas.")

class Asesino(ClasePersonaje):
    def habilidad_especial(self, personaje): pass
        # Los asesinos tienen más poder de ataque
        #print(f"{personaje.nombre} es un Asesino y tiene un alto poder de ataque.")

class Curandero(ClasePersonaje):
    def habilidad_especial(self, personaje):
        # Los curanderos pueden curarse a sí mismos
        print(f"{personaje.nombre} es un Curandero y puede curarse.")
        personaje.vidas += 10
        print(f"{personaje.nombre} se ha curado. Vida actual: {personaje.vidas}")
        time.sleep(3)  # Tiempo de espera para la curación
# %%
# Ejemplo de uso
if __name__ == "__main__":
    # Crear un director
    director = Director()

    # Procesar el archivo JSON
    director.procesar('laberintos/lab4Hab2Bomb2Arm.json')

    # Obtener el juego
    juego = director.obtenerJuego()
# %%
    # Abrir todas las puertas del laberinto
    juego.abrirPuertas()

# %%
    # Crear un visitante para activar bombas
    visitor = VisitorActivarBombas()

    # Aceptar el visitante en el laberinto para activar bombas
    juego.laberinto.aceptar(visitor)

    # Crear un personaje de ejemplo
    juego.agregarPersonaje("Heroe", "Curandero")
# %%
    # Lanzar todos los bichos
    juego.lanzarBichos()

    #juego.terminarBichos()
# %%
    # Obtener comandos
    personaje = juego.person

    for i in personaje.obtenerComandos():
        print(i)

    comandos = personaje.obtenerComandos()

    visitor_inventario = VisitorInventario()

    print(f"Vida del personaje: {personaje.vidas}")
# %%
    # Moverse
    personaje.irAlNorte()
    personaje.irAlSur()
    personaje.irAlEste()
    personaje.irAlOeste()

    # Comandos
    comandos[0].ejecutar(personaje)
    comandos[1].ejecutar(personaje)
    comandos[2].ejecutar(personaje)

    for i in personaje.obtenerComandos():
        print(i)
    comandos = personaje.obtenerComandos()

    # Acciones
    personaje.atacar()  # Atacar sin arma a un bicho si está presente
    personaje.inventario.aceptar(VisitorInventario())  # Listar inventario
    personaje.curarse()  # Curarse si es un curandero
# %%
