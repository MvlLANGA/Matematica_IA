#Exercicio de percentis

import numpy as np  
import matplotlib.pyplot as plt

# Conjunto de números
numeros = [10,12,12,15,18,20,22,100]

# Quartis (Q1 = 25%, Q2 = 50% ou mediana, Q3 = 75%)
Q1 = np.percentile(numeros, 25)
Q2 = np.percentile(numeros, 50)
Q3 = np.percentile(numeros, 75)

print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")

# Média e desvio padrão
media = np.mean(numeros)
desvio = np.std(numeros)
print("média: ", media )
print("Desvio padrão:", desvio)  

# Detecta outliers: valores que estão a mais de 2 desvios padrão da média
outliers = [x for x in numeros if abs(x-media) > 2*desvio]
# x for in numeros percorre todos os valores da lista de dados
#if abs(x-media) calcula a diferença entre o valor x e a média
# > 2*desvio é o desvio padrão no caso o (100)
print("Outliers: ", outliers)

# Cria um boxplot
plt.boxplot(numeros, vert=False, patch_artist=True)

# Título e rótulos
plt.title("Boxplot de numeros com outlier")
plt.xlabel("Valores")
plt.grid(True)
# Mostrar o gráfico
plt.show()
