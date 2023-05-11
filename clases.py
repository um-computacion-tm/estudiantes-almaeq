#aca va la clase
class Persona:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.asistencia = 0
    def cambiar_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self,nombre,email,nro_prof):
        self.nro_prof = nro_prof
        super().__init__(nombre,email)

class Alumno(Persona):
    def __init__(self, nombre, email,legajo):
        self.legajo = legajo
        super().__init__(nombre,email)
        self.materias_cursando = []
    def agregar_materia(self,materia):
        self.materias_cursando.append(materia)

class Materia:
    def __init__(self,cod, nombre,carga):
        self.codigo = cod
        self.nombre = nombre
        self.carga = carga
    def __repr__(self) -> str:
        return "Materia: " + self.nombre


#aca van los objetos
profesor_pepe = Profesor("Pepe","jose@um.edu.ar","2787")
profesor_walter = Profesor("Walter","dff","134")
profesor_daniel = Profesor("Daniel","fdg","346")
alumno_1 = Alumno("Alma Quinteros", "alma.quinteros@gmail.com", 62016)
materia_1 = Materia("0001", "calculo","6hs")
alumno_1.agregar_materia(materia_1)

print(repr(alumno_1.materias_cursando))
print(alumno_1.legajo)
print(alumno_1.nombre)
print(alumno_1.email)
print(materia_1.nombre)
print("el nombre es: ",profesor_pepe.nombre)
print("el email es: ",profesor_pepe.email)
print("la asistencia es: ",profesor_pepe.asistencia)
print("el profesor fue a clase ")
profesor_pepe.asistencia_clase()
print("la asistencia es: ",profesor_pepe.asistencia)
print(profesor_walter.nombre)
print(profesor_daniel.nombre)

profesor_pepe.cambiar_nombre("Jose")
print(profesor_pepe.nombre)