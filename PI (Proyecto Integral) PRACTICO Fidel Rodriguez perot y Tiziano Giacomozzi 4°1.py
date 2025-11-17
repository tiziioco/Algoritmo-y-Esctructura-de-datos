import pandas as pd 
datos_matriz = [
    [101, 'Ana García', '2024-05-01', 95, 120.5],
    [102, 'Luis Pérez', '2024-05-01', 88, 155.0],
    [103, 'Sofía Díaz', '2024-05-01', 98, 115.3],
    [104, 'Juan Soto', '2024-05-01', 75, 180.2],
    [105, 'María López', '2024-05-01', 92, 135.7],
    [101, 'Ana García', '2024-05-15', 99, 110.1],
    [102, 'Luis Pérez', '2024-05-15', 80, 170.5],
    [103, 'Sofía Díaz', '2024-05-15', 90, 140.8],
    [106, 'Pedro Rey', '2024-05-15', 85, 160.0],
    [107, 'Elena Cruz', '2024-05-15', 100, 105.9],
    [108, 'Mario Sol', '2024-05-30', 70, 190.4],
    [109, 'Laura Mar', '2024-05-30', 96, 125.0],
    [110, 'David Luna', '2024-05-30', 89, 145.1],
    [111, 'Gaby Ríos', '2024-05-30', 94, 130.6],
    [112, 'Hector Paz', '2024-05-30', 83, 175.9],
    [103, 'Sofía Díaz', '2024-05-30', 97, 118.2],
    [101, 'Ana García', '2024-05-30', 91, 150.3],
    [113, 'Isabel Vera', '2024-06-15', 93, 132.5],
    [114, 'Carlos Lima', '2024-06-15', 87, 165.4],
    [115, 'Julia Faro', '2024-06-15', 99, 108.7]
]

columnas = ['ID_Alumno', 'Nombre', 'Fecha', 'Puntaje', 'Tiempo_Respuesta (s)']

print("Datos cargados en una matriz de Python.")
print("-" * 40)

while True:
    try:
        puntaje_minimo = int(input("Ingrese el Puntaje Mínimo deseado (ej. 95): "))
        if 0 <= puntaje_minimo <= 100:
            break
        else:
            print("El puntaje debe estar entre 0 y 100. Intente de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

print("-" * 40)
print(f"Buscando alumnos con Puntaje >= {puntaje_minimo}...")
print("-" * 40)
resultados = []
columna_puntaje_idx = 3 

for registro in datos_matriz:
    puntaje = registro[columna_puntaje_idx]
    
    if puntaje >= puntaje_minimo:
        resultados.append(registro)

if resultados:
    print(f" Se encontraron {len(resultados)} registros que cumplen la condición:")
    df_resultados = pd.DataFrame(resultados, columns=columnas)
    
    print("\nResultados filtrados:")
    print(df_resultados)
else:
    print(" No se encontraron registros con el puntaje mínimo ingresado.")