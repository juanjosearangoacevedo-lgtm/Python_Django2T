class Vehiculo:
    def __init__(self, marca, modelo, capacidad):
        self._marca = marca
        self._modelo = modelo
        self._capacidad = capacidad

    
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def capacidad(self):
        return self._capacidad

    
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @capacidad.setter
    def capacidad(self, valor):
        if valor > 0:
            self._capacidad = valor
        else:
            raise ValueError("La capacidad debe ser positiva.")

    
    def moverse(self):
        return "El vehículo se está moviendo."

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Capacidad: {self.capacidad}"
