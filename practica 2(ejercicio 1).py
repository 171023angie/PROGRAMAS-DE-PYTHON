class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro '{self.titulo}' de {self.autor} creado.")

    def mostrar_info(self):
        print("=== Información del Libro ===")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

    def __del__(self):
        print(f"Libro '{self.titulo}' eliminado de la biblioteca.")


# Programa principal
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro1.mostrar_info()

# Eliminar objeto
del libro1
