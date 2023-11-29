# función para validar si la matriz y la fila son válidas
def validar_matriz_y_fila(matriz, fila):
    # Validar si la matriz no está vacía
    if not matriz:
        raise ValueError("La matriz ingresada está vacía.")
    # Validar si la fila especificada es válida para la matriz
    if not (0 <= fila < len(matriz)):
        raise ValueError("La fila especificada no es válida para la matriz.")
# función para sumar los elementos de una fila dada
def suma_fila(matriz, fila):
    # función de validación para asegurarse de que la matriz y la fila sean válidas
    validar_matriz_y_fila(matriz, fila)
    # Inicializar la suma de la fila
    suma = sum(matriz[fila])
    return suma
matriz_ejemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
fila_dada = 1  # Cambiar el índice de fila según sea necesario
try:
    # Intentar sumar los elementos de la fila especificada
    suma_fila_resultante = suma_fila(matriz_ejemplo, fila_dada)
    # Imprimir la suma de la fila resultante
    print(f"Suma de la fila {fila_dada}: {suma_fila_resultante}")
except ValueError as e:
    print(e)
