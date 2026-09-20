class Estudiante:
    """
    Clase que representa a un estudiante.
    ideal para mostrar cómo nacen los atributos.
    """

    # 1. El Consturctor siempre se llama __init__
    # 2. 'self' SIEMPRE es el primer parametro, seguido de los datos que recibe
    def __init__(self, nombre, matricula):
        # Asi se declaran los atributos de la clase (usando self.)
        self.nombre = nombre
        self.matricula = matricula
        self.materias_aprobadas = materias_aprobadas = (
            0  # Atributo de inicializacion por defecto
        )

    def aprobar_materia(self):
        # Si olvidamos el 'self', Python pensará que es una variable local
        # y fallará. Siempre debe llevar self
        self.materias_aprobadas += 1

    def mostrar_info(self):
        return f"El alumno {self.nombre} ha aprobado {self.materias_aprobadas} materias"


# =============================================
# COMO USAR  LA CLASE (fuera de la definicion)
# ==============================================
if __name__ == "__main__":
    # 3. Creacion del objeto (instanciacion) SIN la palabra 'new'
    alumno1 = Estudiante("Carlos", "19001234")
    alumno2 = Estudiante("Ana", "19005678")

    # Al llamar a los metodos, NO le pasamos el primer parametro 'self'
    # Python lo inyecta de forma invisible por debajo del agua
    alumno1.aprobar_materia()
    alumno2.aprobar_materia()

    print(alumno1.mostrar_info())
    print(alumno2.mostrar_info())
