
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    # def getNombre():
    def getNombreAlumno(self):
        return self.nombre

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
    # def getNombre():
    def getNombreProfesor(self):
        return self.nombre

class Materias:
    def __init__(self, materias):
        self.materias = materias

    def getMaterias(self):
        self.materias

a1 = Alumno("Matias Anoniz")
materiasDeAlumnos = Materias({"Programacion", "Matematicas", "Ingles", "Robotica"})

# print ("El nombre del alumno es %s", % (a1.getNombreAlumno()))
# print ("El alumno tiene asignada las siguientes materias: %s", % (a1.getMaterias()))

print(a1.getNombreAlumno())
print(materiasDeAlumnos.getMaterias())

p1 = Profesor("Lucas Blais")
materiasDeProfesores = Materias(["Python", "Android", "Java"])

# print ("El nombre del alumno es %s", % (p1.getNombreProfesor()))
# print ("El Profesor tiene asignada las siguientes Materias:  %s", % (p1.getMaterias()))

print(p1.getNombreProfesor())
print(materiasDeProfesores.getMaterias())
