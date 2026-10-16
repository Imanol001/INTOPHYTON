# REGISTRAR CALIFICACIONES DE VARIOS ALUMNOS


class SistemaCalificaciones:

    def __init__(self, alumnos, materias):
        self.alumnos = alumnos
        self.materias = materias
        self.matriz = []

    def llenar_matriz(self):
        for a in range(self.alumnos):
            fila_temporal = []

            print("\nAlumno", a + 1)

            for m in range(self.materias):
                calificacion = float(
                    input(f"Ingresa la calificacion de la materia {m + 1}:")
                )
                fila_temporal.append(calificacion)

            self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        print("\n===MATRIZ DE CALIFICACIONES===")

        for f in range(self.alumnos):
            for c in range(self.materias):
                print(self.matriz[f][c], "\t", end="")
            print()

    def mostrar_promedios(self):
        print("\n===PROMEDIO DE CADA ALUMNO===")

        for f in range(self.alumnos):
            promedio = sum(self.matriz[f]) / len(self.matriz[f])
            print("Promedio del alumno", f + 1, ":", promedio)

    def mostrar_mayor_menor(self):
        todas_calificaciones = []

        for f in range(self.alumnos):
            for c in range(self.materias):
                todas_calificaciones.append(self.matriz[f][c])

        print("\nCalificacion mas alta:", max(todas_calificaciones))
        print("Calificacion mas baja:", min(todas_calificaciones))


def ejecutar_programa():
    print("=== SISTEMA DE CALIFICACIONES ===")

    alumnos = int(input("Ingresa la cantidad de alumnos: "))
    materias = int(input("Ingresa la cantidad de materias: "))
    sistema = SistemaCalificaciones(alumnos, materias)

    sistema.llenar_matriz()
    sistema.mostrar_matriz()
    sistema.mostrar_promedios()
    sistema.mostrar_mayor_menor()


if __name__ == "__main__":
    ejecutar_programa()
