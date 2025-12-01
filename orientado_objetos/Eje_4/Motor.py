from Eje_4.Motor import Motor
class Automovil:
    def __init__(self, modelo: str, marca: str, anio: int, color: str, motor: Motor):
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.color = color
        self.motor = motor   # Relación de composición con Motor

    def mostrar_informacion(self):
        print("----- Información del Automóvil -----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print("----- Motor -----")
        print(f"Cilindraje: {self.motor.cilindraje}")
        print(f"Combustible: {self.motor.tipo_combustible}")
        print(f"Potencia: {self.motor.potencia} HP")


# Ejemplo de uso:
motor1 = Motor(cilindraje=2.0, tipo_combustible="Gasolina", potencia=150)
auto1 = Automovil(modelo="Focus", marca="Ford", anio=2020, color="Rojo", motor=motor1)

auto1.mostrar_informacion()

auto1.motor.encender()
auto1.motor.acelerar()
auto1.motor.apagar()
