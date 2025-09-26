# Sistema de Gestión de Biblioteca Personal

# ---------- Datos iniciales ----------
generos = ["Novela", "Ciencia Ficción", "Historia", "Programación"]

# Diccionario donde la clave será una tupla (titulo, autor) y el valor será una lista [año, genero, estado]
# estado = "Leído" o "Pendiente"
biblioteca = {}

# ---------- Funciones ----------
def agregar_libro(titulo, autor, año, genero, estado="Pendiente"):
    """Agrega un libro a la biblioteca"""
    clave = (titulo, autor)
    biblioteca[clave] = [año, genero, estado]

def mostrar_libros():
    """Muestra todos los libros en la biblioteca"""
    for libro, datos in biblioteca.items():
        print(f" {libro[0]} - {libro[1]} | Año: {datos[0]}, Género: {datos[1]}, Estado: {datos[2]}")

def marcar_como_leido(titulo, autor):
    """Cambia el estado de un libro a 'Leído'"""
    clave = (titulo, autor)
    if clave in biblioteca:
        biblioteca[clave][2] = "Leído"

def libros_por_estado(estado):
    """Devuelve todos los libros con un estado específico"""
    return [libro for libro, datos in biblioteca.items() if datos[2] == estado]

def libros_por_estado_como_matriz(estado):
    """Devuelve una matriz (lista de listas) con la info completa de los libros con un estado específico."""
    matriz_libros = []
    for (titulo, autor), (año, genero, estado_actual) in biblioteca.items():
        if estado_actual == estado:
            matriz_libros.append([titulo, autor, año, genero])
    return matriz_libros

def generos_disponibles():
    """Devuelve un conjunto de todos los géneros en la biblioteca"""
    return set([datos[1] for datos in biblioteca.values()])

# ---------- Ejecución ----------
if __name__ == "__main__":
    # Agregar libros
    agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela")
    agregar_libro("1984", "George Orwell", 1949, "Ciencia Ficción")
    agregar_libro("Historia de Roma", "Indro Montanelli", 1959, "Historia")
    agregar_libro("Python para Todos", "Raúl González Duque", 2010, "Programación")

    print("Lista de libros en la biblioteca:")
    mostrar_libros()

    print("\nMarcando '1984' como leído...")
    marcar_como_leido("1984", "George Orwell")

    print("\nLibros leídos (Tuplas):")
    for libro in libros_por_estado("Leído"):
        print(f" {libro[0]} - {libro[1]}")

    print("\nLibros leídos (Matriz - Lista de Listas):")
    matriz_leidos = libros_por_estado_como_matriz("Leído")
    for fila in matriz_leidos:
        print(f" {fila}")

    print("\nGéneros disponibles en la biblioteca:", generos_disponibles())