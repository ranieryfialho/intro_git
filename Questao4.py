# Faça uma lista que tenha 100 números aleatórios entre 0 a 100
import random

lista_numerica = []

for i in range(100):
    numero_aleatório = random.randint(1,100)
    lista_numerica.append(numero_aleatório)

print(lista_numerica)