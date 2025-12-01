from Eje_8.vehiculo import Vehiculo
class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, capacidad, num_ruedas):
        super().__init__(marca, modelo, capacidad)
        self._num_ruedas = num_ruedas

    
    @property
    def num_ruedas(self):
        return self._num_ruedas

    
    @num_ruedas.setter
    def num_ruedas(self, valor):
        if valor > 0:
            self._num_ruedas = valor
        else:
            raise ValueError("El número de ruedas debe ser positivo.")

    
    def manejar(self):
        return "El vehículo terrestre está siendo manejado."

    def frenar(self):
        return "El vehículo terrestre está frenando."

    def moverse(self):
        return "El vehículo terrestre avanza por la carretera."

    def __str__(self):
        base = super().__str__()
        return f"{base}, Ruedas: {self.num_ruedas}"
