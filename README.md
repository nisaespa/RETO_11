# RETO 11
## Operaciones de matrices

Los ejercicios del repositorio 11 se encuentran en el archivo `notebook`.

## Primer punto:
```python
# Función para validar si las matrices son adecuadas para realizar operaciones.
def validar(matriz_a, matriz_b):
  # Verificar si las matrices tienen la misma cantidad de filas.
  if len(matriz_a) != len(matriz_b):
    print("Las matrices deben tener el mismo tamaño.")
    return False
  # Verificar que cada elemento de las matrices sea una lista.
  for fila in matriz_a:
    if not isinstance(fila, list):
      print("Las matrices deben ser de tipo numérico.")
      return False
    # Verificar que cada elemento dentro de las listas sea de tipo numérico.
    for elemento in fila:
      if not isinstance(elemento, (int, float)):
        print("Las matrices deben ser de tipo numérico.")
        return False
  # Si todas las validaciones pasan, devolver True.
  return True
# Función para sumar dos matrices.
def sumar_matrices(matriz_a, matriz_b):
  # Validar las matrices antes de realizar la operación.
  if not validar(matriz_a, matriz_b):
    return None
  # Inicializar la matriz resultado como una lista vacía.
  matriz_resultado = []
  # Iterar sobre las filas de ambas matrices simultáneamente.
  for fila_a, fila_b in zip(matriz_a, matriz_b):
    # Sumar los elementos correspondientes de cada fila y agregarlos a la matriz resultado.
    matriz_resultado.append([a + b for a, b in zip(fila_a, fila_b)])
  # Devolver la matriz resultado.
  return matriz_resultado
# Función para restar dos matrices.
def resta(matriz_a, matriz_b):
  # Validar las matrices antes de realizar la operación.
  if not validar(matriz_a, matriz_b):
    return None
  # Inicializar la matriz resultado como una lista vacía.
  matriz_resultado = []
  # Iterar sobre las filas de ambas matrices simultáneamente.
  for fila_a, fila_b in zip(matriz_a, matriz_b):
    # Restar los elementos correspondientes de cada fila y agregarlos a la matriz resultado.
    matriz_resultado.append([a - b for a, b in zip(fila_a, fila_b)])
  # Devolver la matriz resultado.
  return matriz_resultado
# Bloque principal para probar las funciones.
if __name__ == "__main__":
  # Ejemplo de suma de matrices.
  matriz_a = [[1, 2, 3], [4, 5, 6]]
  matriz_b = [[7, 8, 9], [10, 11, 12]]
  matriz_suma = sumar_matrices(matriz_a, matriz_b)
  print("Matriz sumada:")
  for fila in matriz_suma:
    print(fila)
  # Ejemplo de resta de matrices.
  matriz_a = [[1, 2, 3], [4, 5, 6]]
  matriz_b = [[7, 8, 9], [10, 11, 12]]
  matriz_resta = resta(matriz_a, matriz_b)
  print("Matriz restada:")
  for fila in matriz_resta:
    print(fila)
```

## Segundo punto:
```python
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
```
## Tercer punto:
```python
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
```
## Cuarto punto:
```python
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
```
## Quinto punto:
```python
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
```
