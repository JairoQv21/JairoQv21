# Escribe una función para buscar un elemento en una matriz y devolver su índice, o -1 si no se encuentra


# CASE ONE 1
matriz = [1,2,3,4,5]
element = 6

if element in matriz:
    found = matriz.index(element)
    print(found)
    
else:
    print("Elemento no encontrado en matriz")
    
    

### CASE TWO 2
matriz_b = [
    [2,1,3],
    [32,4,6],
    [2,5]
]
element_b = 5

if element_b in matriz_b[0]:
    found = matriz_b[0].index(element_b)
    print(found)
    
elif element_b in matriz_b[1]:
    found = matriz_b[1].index(element_b)
    print(found)
    
elif element_b in matriz_b[2]:
    found = matriz_b[2].index(element_b)
    print(found)
    
    
    
    
### CASE THREE 3
def search_element (matriz, element):
    
    for i in range(len(matriz)):
        if element in matriz[i]:
            return f"({i}, {matriz[i].index(element)})"
        elif element not in matriz:
            return -1
        
        
if __name__ == "__main__":
    
    matriz = [
        [2,1,3],
        [32,4,6],
        [2,5]
        ]
    
    element = 3
    print(search_element(matriz,element))