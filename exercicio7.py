import statistics 
import numpy as np
import random

numeros = [random.randint(1,50) for _ in range(10)] # Usamos o random.randint para fazer uma seleção automatica de 10 numeros aleatórios.
print("lista de numero: ", numeros)



print(f"A media é: ", statistics.mean(numeros)) # mean é media dos nossos numeros
print(f"A mediana é: ", statistics.median(numeros)) # median nos mostar sempre o numero do meio da lista
#no caso de uma lista com numeros pares ele oredena a lista soma os dois numeros do centro e tira a média deles.
print(f"A moda é: ", statistics.multimode(numeros)) #Moda é o numero que mais aparece na nossa lista.