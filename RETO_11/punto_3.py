# función para validar si la matriz puede ser transpuesta
def validar_matriz(matriz):
    # Validar si la matriz no está vacía
    if not matriz:
        raise ValueError("La matriz ingresada está vacía.")
    # Validar si todas las filas tienen la misma longitud
    longitud_fila = len(matriz[0])
    if not all(len(fila) == longitud_fila for fila in matriz):
        raise ValueError("La matriz ingresada no es válida. Las filas deben tener la misma longitud.")
# función para obtener la matriz transpuesta
def matriz_transpuesta(matriz):
    # Llamar a la función de validación para asegurarse de que la matriz pueda ser transpuesta
    validar_matriz(matriz)
    # Calcular la matriz transpuesta intercambiando filas y columnas
    transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
    return transpuesta
matriz_ingresada = [[1, 2, 3],
                    [4, 5, 6]]
try:
    # Intentar obtener la matriz transpuesta
    matriz_transpuesta_resultante = matriz_transpuesta(matriz_ingresada) 
    # Imprimir la matriz transpuesta resultante
    print("Matriz transpuesta:")
    for fila in matriz_transpuesta_resultante:
        print(fila)
except ValueError as e:
    print(e)
