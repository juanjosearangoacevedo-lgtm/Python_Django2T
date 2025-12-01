from .animales import Animal
class Ave(Animal):
    def __init__(self, nombre, edad, especie, alas):
        super().__init__(nombre, edad, especie)
        self._alas = alas

    @property
    def alas(self):
        return self._alas

    @alas.setter
    def alas(self, valor):
        self._alas = valor

    def volar(self):
        return f"{self.nombre} está volando."

    def __str__(self):
        return super().__str__() + f" | Alas: {self.alas}"
