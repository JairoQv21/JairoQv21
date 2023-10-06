# Escribe una función para invertir una matriz en su lugar (sin crear una nueva matriz)

# CASE ONE 1
matriz_a = [
    [2,3,5],
    [7,12,3],
    [13,8,0]
]


matriz_a[0].reverse()
matriz_a[1].reverse()
matriz_a[2].reverse()
print(matriz_a)




# CASE TWO 2
lista = []
for i in reversed(matriz_a[0]):
    lista.append(i)
matriz_a[0] = lista


for j in reversed(matriz_a[1]):
    lista.append(j)
matriz_a[1] = lista





# CASE THREE 3
def matriz_reversed (matriz):
    for i in range(0,len(matriz)):
        matriz[i].reverse()
    return matriz    

matriz_b = [
    [1,5,2],
    [6,12,13],
    [15,18,10]
]

print(matriz_reversed(matriz_b))


# CASE FIVE 5

listilla = [6,12,3]
listilla_b  = []

for x in range(-1,-(len(listilla)+1),-1):
    listilla_b.append(listilla[x])
listilla = listilla_b
print(listilla)
    


# CASE SIX 6 (COMPLETE)
def reversion_lista(input_lista):
    provisional_list = []
    for i in range(-1,-(len(input_lista)+1),-1):
        provisional_list.append(input_lista[i])
    input_lista = provisional_list
    return input_lista
    
def matriz_reversed_b (matriz):    
    for i in range(0,len(matriz)):
        matriz[i] = reversion_lista(matriz[i])
    return matriz 
        

if __name__ == "__main__":
    
    matriz_c = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    result = reversion_lista(matriz_c[0])

    print(result)
