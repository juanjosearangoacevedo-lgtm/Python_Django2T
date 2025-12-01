class Jaula:
    def __init__(self):
        self._animales = []    
        self._cuidador = None  

    @property
    def animales(self):
        return self._animales

    @property
    def cuidador(self):
        return self._cuidador

    @cuidador.setter
    def cuidador(self, valor):
        self._cuidador = valor

    def asignarCuidador(self, cuidador):
        self._cuidador = cuidador

    def asignarAnimal(self, animal):
        self._animales.append(animal)

    def retirarAnimal(self, animal):
        if animal in self._animales:
            self._animales.remove(animal)

    def __str__(self):
        texto = "Jaula:\n"
        if self.cuidador:
            texto += f"  Cuidador: {self.cuidador.nombre_cuidador}\n"
        else:
            texto += "  Cuidador: No asignado\n"

        texto += "  Animales:\n"
        if self.animales:
            for a in self.animales:
                texto += "   - " + str(a) + "\n"
        else:
            texto += "   (Vacía)"
        return texto
