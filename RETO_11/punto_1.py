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
