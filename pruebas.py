from io import StringIO
import sys
import unittest
from juego import *

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.director = Director()
        cls.director.procesar('laberintos/lab4Hab2Bomb2Arm.json')
        cls.juego = cls.director.obtenerJuego()
        # Agregamos un personaje
        cls.juego.agregarPersonaje("Heroe", "Curandero")
        cls.personaje = cls.juego.person
        # Abrimos puertas
        cls.juego.abrirPuertas()
        # Activamos bombas
        cls.visitor = VisitorActivarBombas()
        cls.juego.laberinto.aceptar(cls.visitor)
        #Creamos visitor del inventario
        cls.visitor_inventario = VisitorInventario()

class TestJuegoYLaberinto(BaseTestCase):
    def test_01_juego_y_laberinto_no_son_none(self):
        self.assertIsNotNone(self.juego, "El juego no debería ser None")
        self.assertIsNotNone(self.juego.laberinto, "El laberinto no debería ser None")

    def test_02_estructura_laberinto(self):
        num_habitaciones = len(self.juego.laberinto.hijos)
        self.assertEqual(num_habitaciones, 5, "El laberinto debería tener 4 habitaciones")

        for habitacion in self.juego.laberinto.hijos:
            self.assertIsInstance(habitacion, Habitacion, "Cada elemento debería ser una instancia de Habitacion")

            for hijo in habitacion.hijos:
                self.assertTrue(isinstance(hijo, (Armario, Bomba, Tunel, Arma, Pocion, Llave)), "Los hijos de la habitación deben ser instancias de Armario, Bomba, Tunel, Arma, Pocion o Llave")

class TestInventarioYPocion(BaseTestCase):
    def test_03_personaje_tiene_inventario(self):
        self.assertIsNotNone(self.personaje.inventario, "El personaje debería tener un inventario")

    def test_04_recoger_pocion(self):
        # Obtener comandos
        self.personaje.irAlSur()
        lista = self.personaje.obtenerComandos()

        # Obtener la pocion
        hab2 = self.juego.laberinto.hijos[1]
        pocion = hab2.hijos[2]

        # Verificar que su comando está en la lista de comandos
        self.assertIn(pocion.comandos[0], lista, "El comando recoger debería estar en la lista de comandos del personaje")
        
        # Recoger la pocion
        pocion.comandos[0].ejecutar(self.personaje)
        
        # Verificar que el objeto está en el inventario
        self.assertIn(pocion, self.personaje.inventario.elementos, "La poción debería estar en el inventario del personaje")

        # Obtener el comando de la poción
        comando = pocion.comandos[0]

        # Verificar que el comando es una instancia de Usar
        self.assertIsInstance(comando, Usar, "El comando de la poción debería ser una instancia de Usar")

    def test_05_listar_objetos_con_visitor(self):
        # Crear un StringIO para capturar la salida
        captured_output = StringIO()
        sys.stdout = captured_output

        # Listar los objetos del inventario usando el visitor
        self.personaje.inventario.aceptar(self.visitor_inventario)

        # Restaurar stdout
        sys.stdout = sys.__stdout__

        # Obtener la salida capturada
        output = captured_output.getvalue()

        # Verificar que la salida contiene la información del objeto recogido
        self.assertIn("Pocion", output, "La salida debería contener la información de la poción")

    def test_06_usar_pocion(self):
        pocion = self.personaje.inventario.elementos[0]

        # Verificar que la poción está en el inventario
        self.assertIn(pocion, self.personaje.inventario.elementos, "La poción debería estar en el inventario del personaje")

        # Usar la poción
        pocion.comandos[0].ejecutar(self.personaje)

        # Verificar que la poción ya no está en el inventario
        self.assertNotIn(pocion, self.personaje.inventario.elementos, "La poción debería haber sido usada y no estar en el inventario")

class TestArmas(BaseTestCase):
    def test_07_recoger_arma(self):
        # Obtener comandos
        self.personaje.irAlSur()
        lista = self.personaje.obtenerComandos()

        # Obtener el arma
        hab2 = self.juego.laberinto.hijos[1]
        arma1 = hab2.hijos[0]
        arma2 = hab2.hijos[1]

        # Verificar que su comando está en la lista de comandos
        self.assertIn(arma1.comandos[0], lista, "El comando recoger debería estar en la lista de comandos del personaje")
        self.assertIn(arma2.comandos[0], lista, "El comando recoger debería estar en la lista de comandos del personaje")
        
        # Recoger el arma
        arma1.comandos[0].ejecutar(self.personaje)
        arma2.comandos[0].ejecutar(self.personaje)
        
        # Verificar que el objeto está en el inventario
        self.assertIn(arma1, self.personaje.inventario.elementos, "El arma debería estar en el inventario del personaje")
        self.assertIn(arma2, self.personaje.inventario.elementos, "El arma debería estar en el inventario del personaje")

        # Obtener el comando del arma
        comando1 = arma1.comandos[0]
        comando2 = arma2.comandos[0]

        # Verificar que el comando es una instancia de Atacar
        self.assertIsInstance(comando1, Atacar, "El comando del arma debería ser una instancia de Usar")
        self.assertIsInstance(comando2, Atacar, "El comando del arma debería ser una instancia de Usar")

    def test_08_atacar_arma_robabicho(self):
        # Guardar el estado inicial del personaje y del bicho
        arma = self.personaje.inventario.elementos[0]
        bicho = self.juego.bichos[2]

        vidaPersonaje = self.personaje.vidas
        vidaBicho = bicho.vidas

        # Atacar la poción
        arma.comandos[0].ejecutar(self.personaje)

        # Verificar la vida del bicho
        self.assertEqual(vidaBicho - self.personaje.poder, bicho.vidas, "El bicho debería haber perdido vida al ser atacado con el arma")
        # Verificar la vida del personaje
        self.assertEqual(vidaPersonaje + arma.vida, self.personaje.vidas, "La vida del personaje debería haber aumentado al atacar con el arma")
        
    def test_09_atacar_arma_chupavida(self):
        # Guardar el estado inicial del personaje y del bicho
        self.personaje.irAlNorte()
        arma = self.personaje.inventario.elementos[1]
        bicho = self.juego.bichos[0]

        vidaPersonaje = self.personaje.vidas
        vidaBicho = bicho.vidas
        print(vidaBicho)

        # Atacar la poción
        arma.comandos[0].ejecutar(self.personaje)

        # Verificar la vida del bicho
        self.assertEqual(vidaBicho - self.personaje.poder, bicho.vidas, "El bicho debería haber perdido vida al ser atacado con el arma")
        # Verificar la vida del personaje
        self.assertEqual(vidaPersonaje - arma.vida, self.personaje.vidas, "La vida del personaje debería haber aumentado al atacar con el arma")
        
class TestLlaveYCandado(BaseTestCase):
    def test_10_comprobar_candado(self):
        # Obtener comandos
        lista = self.personaje.obtenerComandos()

        # Obtener el candado
        hab1 = self.juego.laberinto.hijos[0]
        candado = hab1.forma.norte

        # Verificar que su comando está en la lista de comandos
        self.assertIn(candado.comandos[0], lista, "El comando desbloquear debería estar en la lista de comandos del personaje")
        
        # Verificar que no se puede entrar a la habitación
        posicionInicial = self.personaje.posicion
        self.personaje.irAlNorte()
        self.assertEqual(self.personaje.posicion, posicionInicial, "El personaje no debería poder entrar a la habitación con el candado cerrado")
 
        # Verificar que no se puede desbloquear sin la llave
        candado.comandos[0].ejecutar(self.personaje)
        self.assertEqual(self.personaje.posicion, posicionInicial, "El personaje no debería poder entrar a la habitación con el candado cerrado")

    def test_11_recoger_llave(self):
        # Obtener comandos
        self.personaje.irAlSur()
        self.personaje.irAlEste()
        lista = self.personaje.obtenerComandos()

        # Obtener la llave
        hab3 = self.juego.laberinto.hijos[2]
        llave = hab3.hijos[3]

        # Verificar que su comando está en la lista de comandos
        self.assertIn(llave.comandos[0], lista, "El comando recoger debería estar en la lista de comandos del personaje")
        
        # Recoger la llave
        llave.comandos[0].ejecutar(self.personaje)
        
        # Verificar que el objeto está en el inventario
        self.assertIn(llave, self.personaje.inventario.elementos, "La llave debería estar en el inventario del personaje")

    def test_12_abrir_candado(self):
        # Obtener candado
        self.personaje.irAlOeste()
        self.personaje.irAlNorte()

        hab1 = self.juego.laberinto.hijos[0]
        candado = hab1.forma.norte

        # Verificar que se puede entrar a la habitación
        posicionInicial = self.personaje.posicion
        candado.comandos[0].ejecutar(self.personaje)
        hab5 = self.juego.laberinto.hijos[4]
        self.assertNotEqual(self.personaje.posicion, posicionInicial, "El personaje debería poder entrar a la habitación con la llave")
        self.assertEqual(self.personaje.posicion, hab5, "El personaje debería poder entrar a la habitación con la llave")

class TestPersonaje(BaseTestCase):
    def test_13_comprobar_tanque(self):
        self.juego.agregarPersonaje("Heroe", "Tanque")
        self.personaje = self.juego.person

        # Verificar que el personaje es un tanque
        self.assertTrue(isinstance(self.personaje.clase , Tanque), "El personaje debe ser de clase tanque")
        self.assertEqual(self.personaje.vidas, 70, "El personaje debe tener vidas = 70")
        self.assertEqual(self.personaje.poder, 6, "El personaje debe tener poder = 6")
        
        # Verificar que el tanque resiste bombas
        vidaInicial = self.personaje.vidas
        self.personaje.irAlSur()
        self.personaje.irAlEste()
        self.assertEqual(vidaInicial, self.personaje.vidas, "El tanque debe resistir bombas sin perder vida")

    def test_14_comprobar_asesino(self):
        self.juego.agregarPersonaje("Heroe", "Asesino")
        self.personaje = self.juego.person
        
        # Verificar que el personaje es un tanque
        self.assertTrue(isinstance(self.personaje.clase , Asesino), "El personaje debe ser de clase asesino")
        self.assertEqual(self.personaje.vidas, 40, "El personaje debe tener vidas = 40")
        self.assertEqual(self.personaje.poder, 15, "El personaje debe tener poder = 15")

    def test_15_comprobar_curandero(self):
        self.juego.agregarPersonaje("Heroe", "Curandero")
        self.personaje = self.juego.person

        # Verificar que el personaje es un curandero
        self.assertTrue(isinstance(self.personaje.clase , Curandero), "El personaje debe ser de clase curandero")
        self.assertEqual(self.personaje.vidas, 30, "El personaje debe tener vidas = 30")
        self.assertEqual(self.personaje.poder, 3, "El personaje debe tener poder = 3")
        
        # Verificar que el curandero puede curarse
        vidaInicial = self.personaje.vidas
        self.personaje.curarse()
        self.assertNotEqual(vidaInicial, self.personaje.vidas, "El curandero debe poder curarse y aumentar su vida")

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
