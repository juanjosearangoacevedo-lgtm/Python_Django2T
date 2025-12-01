class Jugador:
    def __init__(self, nombre: str, posicion: float, edad: int, numero_camisa: int):
        self._nombre = nombre
        self._posicion = posicion
        self._edad = edad
        self._numero_camisa = numero_camisa

    # ----- Getters -----
    def get_nombre(self):
        return self._nombre

    def get_posicion(self):
        return self._posicion

    def get_edad(self):
        return self._edad

    def get_numero_camisa(self):
        return self._numero_camisa

    # ----- Setters -----
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_posicion(self, posicion):
        self._posicion = posicion

    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser positiva.")

    def set_numero_camisa(self, numero):
        if numero > 0:
            self._numero_camisa = numero
        else:
            print("El número de camisa debe ser positivo.")

    # ----- Método -----
    def transferir(self, nuevo_equipo):
        print(f"El jugador {self._nombre} ha sido transferido al equipo {nuevo_equipo}.")

