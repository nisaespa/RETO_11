# función para validar si la matriz y la columna son válidas
def validar_matriz_y_columna(matriz, columna):
    # Validar si la matriz no está vacía
    if not matriz:
        raise ValueError("La matriz ingresada está vacía.")
    # Validar si la columna especificada es válida para la matriz
    if not (0 <= columna < len(matriz[0])):
        raise ValueError("La columna especificada no es válida para la matriz.")
# función para sumar los elementos de una columna dada
def suma_columna(matriz, columna):
    # Llamar a la función de validación para asegurarse de que la matriz y la columna sean válidas
    validar_matriz_y_columna(matriz, columna)
    # Inicializar la suma de la columna
    suma = 0
    # Sumar los elementos de la columna especificada
    for fila in matriz:
        suma += fila[columna]
    return suma
matriz_ejemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
columna_dada = 0  # Cambiar el índice de columna según sea necesario
try:
    # Intentar sumar los elementos de la columna especificada
    suma_columna_resultante = suma_columna(matriz_ejemplo, columna_dada)
    # Imprimir la suma de la columna resultante
    print(f"Suma de la columna {columna_dada}: {suma_columna_resultante}")
except ValueError as e:
    print(e)
