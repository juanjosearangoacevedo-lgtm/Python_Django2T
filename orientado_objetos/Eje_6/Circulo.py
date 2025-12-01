from Eje_6.FormaGeometrica import FormaGeometrica
from Eje_6.Rectangulo import Rectangulo
import math
class Circulo(FormaGeometrica):
    def __init__(self, color: str, radio: float):
        super().__init__(color)
        self._radio = radio

    # ----- Getters -----
    def get_radio(self):
        return self._radio

    # ----- Setters -----
    def set_radio(self, radio):
        self._radio = radio

    # Método sobrescrito
    def calcular(self):
        return math.pi * (self._radio ** 2)

    def mostrar(self):
        super().mostrar()
        print(f"Radio: {self._radio}")
        print(f"Área del círculo: {self.calcular()}")


# =============================
# Ejemplo de uso:
# =============================

rect = Rectangulo("Rojo", 10.0, 5.0)
cir = Circulo("Azul", 7.0)

print("------ RECTÁNGULO ------")
rect.mostrar()

print("\n------ CÍRCULO ------")
cir.mostrar()
