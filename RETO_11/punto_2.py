# función para validar si las matrices pueden multiplicarse
def validar_matrices(matriz1, matriz2):
    # Validar si el número de columnas de la primera matriz es igual al número de filas de la segunda matriz
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no son compatibles.")
# función para realizar el producto de matrices
def producto_matrices(matriz1, matriz2):
    # Llamar a la función de validación para asegurarse de que las matrices puedan multiplicarse
    validar_matrices(matriz1, matriz2)
    # Inicializar la matriz resultante con ceros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    # Realizar el producto de matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                # Sumar el producto de los elementos correspondientes de las matrices
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado
matriz_a = [[1, 2, 3],
            [4, 5, 6]]
matriz_b = [[7, 8],
            [9, 10],
            [11, 12]]
# Para validar
try:
    # Intentar calcular el producto de matrices
    resultado_producto = producto_matrices(matriz_a, matriz_b)
    # Imprimir el resultado del producto de matrices
    print("Resultado del producto de matrices:")
    for fila in resultado_producto:
        print(fila)
except ValueError as e:
    print(e)
