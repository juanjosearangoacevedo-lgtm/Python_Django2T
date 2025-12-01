from Eje_7.empleado_hora import EmpleadoTiempoCompleto, Empleado
class Empleado_hora(Empleado):
    def __init__(self, id_empleado: int, nombre: str, salario_base: float, tarifa_por_hora: float, horas_trabajadas: int):
        super().__init__(id_empleado, nombre, salario_base)
        self._tarifa_por_hora = tarifa_por_hora
        self._horas_trabajadas = horas_trabajadas

    # Getters y Setters
    def get_tarifa_por_hora(self):
        return self._tarifa_por_hora

    def get_horas_trabajadas(self):
        return self._horas_trabajadas

    def set_tarifa_por_hora(self, tarifa):
        if tarifa >= 0:
            self._tarifa_por_hora = tarifa
        else:
            print("La tarifa por hora debe ser positiva.")

    def set_horas_trabajadas(self, horas):
        if horas >= 0:
            self._horas_trabajadas = horas
        else:
            print("Las horas trabajadas deben ser positivas.")

    # Sobrescritura del método calcular
    def calcular(self):
        return self._tarifa_por_hora * self._horas_trabajadas


# =====================================
# Ejemplo de uso
# =====================================

empleado1 = EmpleadoTiempoCompleto(1, "Laura Torres", 0, 2500000)
empleado2 = Empleado_hora(2, "Carlos Gómez", 0, 25000, 120)

print("----- EMPLEADO TIEMPO COMPLETO -----")
print(f"Nombre: {empleado1.get_nombre()}")
print(f"Salario mensual: {empleado1.calcular()}")

print("\n----- EMPLEADO POR HORA -----")
print(f"Nombre: {empleado2.get_nombre()}")
print(f"Salario total: {empleado2.calcular()}")
