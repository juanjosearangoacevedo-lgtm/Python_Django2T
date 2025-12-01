from Eje_6.FormaGeometrica import FormaGeometrica
class Rectangulo(FormaGeometrica):
    def __init__(self, color: str, largo: float, ancho: float):
        super().__init__(color)
        self._largo = largo
        self._ancho = ancho

    # ----- Getters -----
    def get_largo(self):
        return self._largo

    def get_ancho(self):
        return self._ancho

    # ----- Setters -----
    def set_largo(self, largo):
        self._largo = largo

    def set_ancho(self, ancho):
        self._ancho = ancho

    # Método sobrescrito
    def calcular(self):
        return self._largo * self._ancho

    def mostrar(self):
        super().mostrar()
        print(f"Largo: {self._largo}")
        print(f"Ancho: {self._ancho}")
        print(f"Área del rectángulo: {self.calcular()}")

