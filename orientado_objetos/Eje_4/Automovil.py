class Motor:
    def __init__(self, cilindraje: float, tipo_combustible: str, potencia: float):
        self.cilindraje = cilindraje
        self.tipo_combustible = tipo_combustible
        self.potencia = potencia
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El motor ha sido encendido.")
        else:
            print("El motor ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El motor ha sido apagado.")
        else:
            print("El motor ya estaba apagado.")

    def acelerar(self):
        if self.encendido:
            print("El motor está acelerando... ¡Vruuum!")
        else:
            print("No puedes acelerar, el motor está apagado.")

