class Animal:
    def __init__(self, nombre, edad, especie):
        self._nombre = nombre
        self._edad = edad
        self._especie = especie

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def especie(self):
        return self._especie

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor
        else:
            raise ValueError("La edad no puede ser negativa.")

    @especie.setter
    def especie(self, valor):
        self._especie = valor

    def hacer_sonido(self):
        return f"{self.nombre} está haciendo un sonido."

    def comer(self):
        return f"{self.nombre} está comiendo."

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.edad} años)"
