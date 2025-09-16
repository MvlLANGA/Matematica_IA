import numpy as np 
import statistics
import matplotlib.pyplot as plt
import random
from collections import Counter

numeros = [12,15,12,18,20,15,22,19,15,10]
print("O desvio padrão é: ", np.std(numeros))
print("A variancia é: ", np.var(numeros))

print("A media é: ", statistics.mean(numeros))
print("A mediana é: ", statistics.median(numeros))
print("A moda é: ", statistics.multimode(numeros))

# frequencia = {x:numeros.count(x) for x in set(numeros)}
frequencia =Counter(numeros)
print("Frequencia: ",frequencia)

#plt.hist(numeros, bins=range(min(numeros), max(numeros)+2), color="green", edgecolor="black")
plt.hist(numeros,color='green', edgecolor='black')
plt.title("Histograma Numeros")
plt.xlabel("numeros")
plt.ylabel("frequencia")
plt.show()
