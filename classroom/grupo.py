

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = 12

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is None:
            self._asignaturas = []

        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if self.listadoAlumnos is None:
            self.listadoAlumnos = []
            if lista is None:
                self.listadoAlumnos = [alumno]
            else:
                for elemento in lista:
                    self.listadoAlumnos.append(elemento)
                self.listadoAlumnos.append(alumno)
        else:
            if lista is None:
                self.listadoAlumnos = [alumno]
            else:
                for elemento in lista:
                    self.listadoAlumnos.append(elemento)
                self.listadoAlumnos.append(alumno)




    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
