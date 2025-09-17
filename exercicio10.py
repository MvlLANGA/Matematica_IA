#Exercicio de percentis

import numpy as np  
import matplotlib.pyplot as plt

# Conjunto de números
numeros = [12,15,12,18,20,15,22,19,15,10]

# Calcula o 1º quartil (25%) → separa os 25% menores valores
Q1 = np.percentile(numeros, 25)

# Calcula o 2º quartil (50%) → mediana, separa metade inferior da superior
Q2 = np.percentile(numeros, 50)

# Calcula o 3º quartil (75%) → separa os 75% menores valores
Q3 = np.percentile(numeros, 75)

# Mostra os resultados formatados
print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")

plt.boxplot(numeros, vert=True, patch_artist=True)

# Título e rótulos
plt.title("Boxplot dos Números")
plt.xlabel("Valores")

# Mostrar o gráfico
plt.show()
