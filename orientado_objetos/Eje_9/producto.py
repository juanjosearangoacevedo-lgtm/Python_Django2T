class Producto:
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self._precio = valor
        else:
            raise ValueError("El precio debe ser positivo.")

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio}"

