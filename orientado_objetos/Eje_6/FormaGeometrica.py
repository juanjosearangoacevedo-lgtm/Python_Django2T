import math

# =============================
# Clase Padre: Forma Geométrica
# =============================
class FormaGeometrica:
    def __init__(self, color: str):
        self._color = color

    # ----- Getters -----
    def get_color(self):
        return self._color

    # ----- Setters -----
    def set_color(self, color: str):
        self._color = color

    # Métodos generales (se sobreescribirán)
    def calcular(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def mostrar(self):
        print(f"Color: {self._color}")

