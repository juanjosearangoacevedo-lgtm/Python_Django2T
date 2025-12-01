from .animales import Animal
class Mamifero(Animal):
    def __init__(self, nombre, edad, especie, tipo_pelaje):
        super().__init__(nombre, edad, especie)
        self._tipo_pelaje = tipo_pelaje

    @property
    def tipo_pelaje(self):
        return self._tipo_pelaje

    @tipo_pelaje.setter
    def tipo_pelaje(self, valor):
        self._tipo_pelaje = valor

    def amamantar(self):
        return f"{self.nombre} está amamantando a sus crías."

    def __str__(self):
        return super().__str__() + f" | Pelaje: {self.tipo_pelaje}"
