from Eje_5.Jugador import Jugador
class Equipo:
    def __init__(self, nombre: str, ciudad: str, entrenador: str):
        self._nombre = nombre
        self._ciudad = ciudad
        self._entrenador = entrenador
        self._jugadores = []   # Lista de Jugador

    # ----- Getters -----
    def get_nombre(self):
        return self._nombre

    def get_ciudad(self):
        return self._ciudad

    def get_entrenador(self):
        return self._entrenador

    def get_jugadores(self):
        return self._jugadores

    # ----- Setters -----
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def set_entrenador(self, entrenador):
        self._entrenador = entrenador

    # ----- Métodos -----
    def agregar(self, jugador: Jugador):
        self._jugadores.append(jugador)
        print(f"Jugador {jugador.get_nombre()} agregado al equipo {self._nombre}.")

    def remover(self, nombre_jugador: str):
        for jugador in self._jugadores:
            if jugador.get_nombre() == nombre_jugador:
                self._jugadores.remove(jugador)
                print(f"Jugador {nombre_jugador} ha sido removido del equipo {self._nombre}.")
                return
        print(f"No se encontró al jugador '{nombre_jugador}' en el equipo.")

    def mostrar(self):
        print(f"\n--- Equipo: {self._nombre} ---")
        print(f"Ciudad: {self._ciudad}")
        print(f"Entrenador: {self._entrenador}")
        print("Jugadores:")
        if len(self._jugadores) == 0:
            print("  No hay jugadores en el equipo.")
        else:
            for jugador in self._jugadores:
                print(f"  - {jugador.get_nombre()} | Posición: {jugador.get_posicion()} | "
                      f"Edad: {jugador.get_edad()} | Camisa: {jugador.get_numero_camisa()}")
        print("-----------------------------------")


# Ejemplo de uso:

jug1 = Jugador("Carlos Pérez", 9.0, 24, 10)
jug2 = Jugador("Juan Rojas", 4.0, 21, 5)

equipo1 = Equipo("Leones FC", "Medellín", "Luis Gómez")

equipo1.agregar(jug1)
equipo1.agregar(jug2)

equipo1.mostrar()

equipo1.remover("Juan Rojas")
equipo1.mostrar()

jug1.transferir("Águilas Doradas")
