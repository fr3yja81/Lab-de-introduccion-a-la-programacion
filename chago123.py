class Docente:
    def __init__(self, idDocente, nombre):
        self.idDocente = idDocente
        self.nombre = nombre

    def __str__(self):
        return f"[{self.idDocente}] {self.nombre}"

class Carrera:
    def __init__(self, sigla, nombre):
        self.sigla = sigla
        self.nombre = nombre
        self.responsable = None  # Aquí se guardará un objeto Docente

    def __str__(self):
        resp = self.responsable.nombre if self.responsable else "Pendiente"
        return f"{self.sigla.ljust(5)} | {self.nombre.ljust(35)} | Responsable: {resp}"

class UnidadAcademica:
    def __init__(self):
        self.listaDocentes = []
        self.director = None
        # Inicialización de carreras solicitadas
        self.carreras = [
            Carrera("IC", "Ingeniería en Computación"),
            Carrera("IS", "Ingeniería de Software"),
            Carrera("IRM", "Ingeniería en Robótica y Mecatrónica"),
            Carrera("IEI", "Ingeniería Eléctrica Industrial")
        ]

    def agregar_docente(self):
        print("\n--- Registro de Docente ---")
        id_d = input("ID/Cédula: ")
        nombre = input("Nombre completo: ")
        self.listaDocentes.append(Docente(id_d, nombre))
        print("Docente registrado exitosamente.")

    def gestionar_roles(self):
        if not self.listaDocentes:
            print("\n¡Error! Primero debe registrar docentes.")
            return

        print("\n--- Gestión de Roles ---")
        print("1. Asignar Director de Unidad")
        print("2. Asignar Responsable de Programa")
        op = input("Seleccione: ")

        # Mostrar docentes disponibles
        print("\nLista de Docentes:")
        for i, d in enumerate(self.listaDocentes):
            print(f"{i}. {d}")
        
        idx = int(input("Seleccione el índice del docente: "))
        docente_elegido = self.listaDocentes[idx]

        if op == "1":
            self.director = docente_elegido
            print(f"Director asignado: {docente_elegido.nombre}")
        elif op == "2":
            print("\nCarreras disponibles:")
            for i, c in enumerate(self.carreras):
                print(f"{i}. {c.nombre}")
            idx_c = int(input("Seleccione la carrera: "))
            self.carreras[idx_c].responsable = docente_elegido
            print(f"Responsable de {self.carreras[idx_c].sigla} asignado: {docente_elegido.nombre}")

    def mostrar_estado(self):
        print("\n" + "="*60)
        print("ESTADO DE LA UNIDAD ACADÉMICA")
        print("="*60)
        dir_nom = self.director.nombre if self.director else "No asignado"
        print(f"DIRECTOR GENERAL: {dir_nom}")
        print("-" * 60)
        print("PROGRAMAS Y RESPONSABLES:")
        for c in self.carreras:
            print(c)
        print("="*60)

def menu():
    sistema = UnidadAcademica()
    while True:
        print("\n--- SISTEMA DE INGENIERÍA ELÉCTRICA ---")
        print("1. Registrar Docente")
        print("2. Gestionar Roles (Director/Responsable)")
        print("3. Ver Estructura Académica")
        print("4. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            sistema.agregar_docente()
        elif opcion == "2":
            sistema.gestionar_roles()
        elif opcion == "3":
            sistema.mostrar_estado()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()