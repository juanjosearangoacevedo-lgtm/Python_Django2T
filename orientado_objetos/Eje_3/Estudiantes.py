class Estudiante:
    def __init__(self, id_estudiante, nombre, carrera):
        self.__id_estudiante = id_estudiante
        self.__nombre = nombre
        self.__carrera = carrera
        self.__listadoCursos = []   

    def get_id_estudiante(self):
        return self.__id_estudiante
    
    def get_nombre(self):
        return self.__nombre
    
    def get_carrera(self):
        return self.__carrera
    
    def get_listadoCursos(self):
        return self.__listadoCursos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def registrar_curso(self, curso):
        """Agrega un curso al estudiante si no está registrado."""
        if curso not in self.__listadoCursos:
            self.__listadoCursos.append(curso)
            curso.agregar_estudiantes(self)  # Relación bidireccional
            print(f"Curso '{curso.get_nombre()}' registrado para {self.__nombre}.")
        else:
            print("El estudiante ya está registrado en este curso.")