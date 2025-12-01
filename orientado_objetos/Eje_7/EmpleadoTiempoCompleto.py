from Eje_7.Empleado import Empleado
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, id_empleado: int, nombre: str, salario_base: float, salario_fijo_mensual: float):
        super().__init__(id_empleado, nombre, salario_base)
        self._salario_fijo_mensual = salario_fijo_mensual

    # Getters y Setters
    def get_salario_fijo_mensual(self):
        return self._salario_fijo_mensual

    def set_salario_fijo_mensual(self, salario):
        if salario >= 0:
            self._salario_fijo_mensual = salario
        else:
            print("El salario mensual debe ser positivo.")

    # Sobrescritura del método calcular
    def calcular(self):
        return self._salario_fijo_mensual

