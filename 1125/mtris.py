


def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto


matriz_a = [
    [10, 3, 6],
    [1, 1, 3],
    [0, 2, 1],
]
matriz_b = [
    [2, 1],
    [1, 0],
    [3, 2],
]
producto = producto_matrices(matriz_a, matriz_b)
if producto:
    # Imprimir resultado
    for fila in producto:
        for valor in fila:
            # imprimir sin salto de línea. Usando un espacio al final
            print(valor, end=" ")
        print("")
else:
    print("El número de columnas de A es distinto al número de filas de B")