def Novel_MCM(p):
    # Inicialmente, el costo total de multiplicación es 0
    C = 0
    N = len(p) - 1  # Número de matrices
    
    # Bucle para encontrar el mínimo entre las multiplicaciones de las matrices diagonales
    while N >= 3:
        k = Find_min(p, N)
        
        # Añadir el costo de la multiplicación de la matriz en la posición k
        C += p[k] * p[k+1] * p[k+2]
        
        # Desplazar las dimensiones de las matrices restantes
        for i in range(k+1, N):
            p[i] = p[i+1]
        N -= 1
        
    return C

# Función para encontrar el mínimo entre las multiplicaciones de matrices diagonales
def Find_min(p, N):
    # Inicialmente, el mínimo es el producto de la primera y tercera matriz
    min_val = p[1] * p[3]
    flag = 1
    
    # Bucle para buscar el mínimo
    for i in range(2, N-1):
        if min_val > p[i] * p[i+2]:
            # Si encontramos un nuevo mínimo, actualizamos min y flag
            min_val = p[i] * p[i+2]
            flag = i
    
    # Devolver el índice donde se encuentra el mínimo
    return flag