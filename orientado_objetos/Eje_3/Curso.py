class Curso:
    def __init__(self, id_curso, nombre, numero_creditos):
        self.__id_curso = id_curso
        self.__nombre = nombre
        self.__numero_creditos = numero_creditos
        self.__listadoEstudiantes = []   

    def get_id_curso(self):
        return self.__id_curso
    
    def get_nombre(self):
        return self.__nombre
    
    def get_numero_creditos(self):
        return self.__numero_creditos
    
    def get_listadoEstudiantes(self):
        return self.__listadoEstudiantes

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_numero_creditos(self, creditos):
        self.__numero_creditos = creditos

    def agregar_estudiantes(self, estudiante):
        """Asocia un estudiante al curso."""
        if estudiante not in self.__listadoEstudiantes:
            self.__listadoEstudiantes.append(estudiante)

    def registrar(self):
        """Muestra la información del curso."""
        print(f"Curso: {self.__nombre} - Créditos: {self.__numero_creditos}")
        print("Estudiantes inscritos:")
        for est in self.__listadoEstudiantes:
            print(f" - {est.get_nombre()}")
