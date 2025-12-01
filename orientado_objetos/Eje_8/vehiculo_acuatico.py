from Eje_8.vehiculo import Vehiculo
class VehiculoAcuatico(Vehiculo):
    def __init__(self, marca, modelo, capacidad, tipo_propulsion):
        super().__init__(marca, modelo, capacidad)
        self._tipo_propulsion = tipo_propulsion

    
    @property
    def tipo_propulsion(self):
        return self._tipo_propulsion

    
    @tipo_propulsion.setter
    def tipo_propulsion(self, valor):
        self._tipo_propulsion = valor

    def manejar(self):
        return "El vehículo acuático está siendo dirigido."

    def anclar(self):
        return "El vehículo acuático ha echado el ancla."

    def moverse(self):
        return "El vehículo acuático navega por el agua."

    def __str__(self):
        base = super().__str__()
        return f"{base}, Propulsión: {self.tipo_propulsion}"