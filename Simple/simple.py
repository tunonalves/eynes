#Simple
import random
lista = []

def age():
    ages = random.randrange(1,100)
    return ages

lista = [
    dict(
        zip([x],[age()])
        ) 
        for x in range(0,10)
    ]

print(lista)

