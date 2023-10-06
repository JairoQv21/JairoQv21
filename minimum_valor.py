
"""import time 
#inicio = time.time()
###############################
time.sleep(1)"""
# Escribe una función para encontrar el valor mínimo en una matriz de números enteros.


# CASE ONE 1
def find_minium_value( matriz):
    
    if not matriz:
        return None
    
    min_value = matriz[0][0]
    
    for row in matriz:
        for value in row:
            if value < min_value:
                min_value = value
                
    return min_value

matriz = [
    [5,2,3],
    [4,5,6],
    [7,8,9]
    ]
min_value_var = find_minium_value(matriz)



# CASE TWO 2
def minimun_valur(lista ):
    
    min = lista[0]

    for i in range(1,len(lista)):
        if min > lista[i]:
            min = lista[i]
    return min
        
lista = [3,4,1,4,5]
print(minimun_valur(lista))



# CASE THREE 3 
matriz_b = [
    [3,2,13],
    [43,5,26,1],
    [12,8,99]
    ]

x = min(matriz_b[0])
y = min(matriz_b[1])
z = min(matriz_b[2])

if y < x and y < z:
    value = y
elif x < z and x < y:
    value = x
elif z < x and z < y:
    value = z

print(value)



# CASE FOUR 4
matriz_c = [
    [3,1,13],
    [43,5,26,2],
    [1,8,-99]
    ]

minimo = min(matriz_c[0])

for i in range(1,len(matriz_c)):
    matriz_c[i].append(minimo)
    minimo = min(matriz_c[i])

print(minimo)




# CASE FIVE 5 
def minimum_value(input_matriz):
    
    if not input_matriz:
        return None
    
    minimum = min(input_matriz[0])
    
    for i in range(1,len(input_matriz)):
        input_matriz[i].append(minimum)
        minimum = min(input_matriz[i])
    return minimum


if __name__ == "__main__":

    input_matriz = [
        [3,13],
        [43,5,26,2],
        [8,99]
        ]

    print(minimum_value(input_matriz))

"""#fin = time.time()
#print(fin-inicio)""" 