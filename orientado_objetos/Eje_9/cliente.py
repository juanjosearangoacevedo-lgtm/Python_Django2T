class Cliente:
    def __init__(self, nombre, email, telefono):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @email.setter
    def email(self, valor):
        self._email = valor

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Tel: {self.telefono}"

