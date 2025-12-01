class Cuidador:
    def __init__(self, nombre_cuidador, anos_exp):
        self._nombre_cuidador = nombre_cuidador
        self._anos_exp = anos_exp

    @property
    def nombre_cuidador(self):
        return self._nombre_cuidador

    @property
    def anos_exp(self):
        return self._anos_exp

    @nombre_cuidador.setter
    def nombre_cuidador(self, valor):
        self._nombre_cuidador = valor

    @anos_exp.setter
    def anos_exp(self, valor):
        if valor >= 0:
            self._anos_exp = valor
        else:
            raise ValueError("Los años de experiencia deben ser positivos.")

    def cuidar(self, animal):
        return f"{self.nombre_cuidador} está cuidando a {animal.nombre}."

    def __str__(self):
        return f"Cuidador: {self.nombre_cuidador} ({self.anos_exp} años de experiencia)"
