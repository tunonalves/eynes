#Matriz
import random

def num_aleatorio():
    num = random.randrange(1,10)
    return num

def matriz():
    lista2 = []
    for i in range(5):
        lista2.append([])
        for j in range(5):
            lista2[i].append(num_aleatorio())	
    matrix_length = len(lista2)
    for i in range(matrix_length):
        print(lista2[i])
    return lista2
    
matriz()