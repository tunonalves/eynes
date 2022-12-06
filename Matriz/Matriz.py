#Matriz
import random


def listaAleatorios():
    lista = [0]
    for i in range(5):
        lista[i] = random.random()
    return lista
    
print(listaAleatorios())