class Empleado:
    def __init__(self, id_empleado: int, nombre: str, salario_base: float):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._salario_base = salario_base

    # ----- Getters -----
    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre(self):
        return self._nombre

    def get_salario_base(self):
        return self._salario_base

    # ----- Setters -----
    def set_id_empleado(self, id):
        self._id_empleado = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_salario_base(self, salario):
        if salario >= 0:
            self._salario_base = salario
        else:
            print("El salario base debe ser positivo.")

    # ----- Método general (abstracto) -----
    def calcular(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

