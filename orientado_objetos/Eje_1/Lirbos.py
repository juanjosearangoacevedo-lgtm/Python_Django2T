class Libro:
    def __init__(self, titulo, autor, anio, num_paginas, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__num_paginas = num_paginas
        self.__disponible = disponible

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio

    def get_num_paginas(self):
        return self.__num_paginas

    def get_disponible(self):
        return self.__disponible

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_anio(self, anio):
        if isinstance(anio, int):
            self.__anio = anio
        else:
            print("El año debe ser un número entero.")

    def set_num_paginas(self, num_paginas):
        if num_paginas > 0:
            self.__num_paginas = num_paginas
        else:
            print("El número de páginas debe ser positivo.")

    def set_disponible(self, disponible):
        if isinstance(disponible, bool):
            self.__disponible = disponible
        else:
            print("El estado 'disponible' debe ser True o False.")

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' no está disponible.")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"El libro '{self.__titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.__titulo}' ya estaba disponible.")
