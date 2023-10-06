# Escribe una función para eliminar un elemento en un índice dado de una matriz y ajustar la matriz para llenar el espacio vacío

# (0,2,5) -> (0,-,5) -> (0,5)


# CASE ONE 1
matriz_a = [
    [2,3,5],
    [7,12,3],
    [13,8,0]
]
posicion_a = 0
posicion_b = 1

matriz_a[posicion_a][posicion_b] = 0

print(matriz_a)



# CASE DOS 2
def delete_posicion(matriz,posicion_a, posicion_b):
    if matriz[posicion_a][posicion_b] == 0:
        matriz[posicion_a][posicion_b] = -1
    else:
        matriz[posicion_a][posicion_b] = 0
    return matriz

if __name__ == "__main__":

    matriz = [
        [3,10,0],
        [4,6,10],
        [19,32,21]
    ]

    print(delete_posicion(matriz,0,2))

