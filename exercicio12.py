import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar números aleatórios entre 0 e 1 (50 x 10 x 100 = 50.000 números)
numeros = np.random.normal(loc=50, scale=10, size=100)

# 3. Criar o histograma
plt.hist(numeros, bins=10, color='orange', edgecolor='black')

# 4. Adicionar rótulos e título
plt.title('Histograma de Números Aleatórios')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.grid(True)

# 5. Mostrar o gráfico
plt.show()

