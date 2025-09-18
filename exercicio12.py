import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar um array de 100 números aleatórios seguindo uma distribuição normal
# Média (loc) = 50, Desvio padrão (scale) = 10
numeros = np.random.normal(loc=50, scale=10, size=100)

# 2. Criar o histograma dos dados gerados
# bins=10 define 10 faixas (intervalos) no histograma
# color='orange' define a cor das barras
# edgecolor='black' adiciona contorno preto nas barras
plt.hist(numeros, bins=10, color='brown', edgecolor='black')

# 3. Adicionar título e rótulos aos eixos
plt.title('Histograma de Números Aleatórios')  # Título do gráfico
plt.xlabel('')                            # Rótulo do eixo X
plt.ylabel('')                       # Rótulo do eixo Y
plt.grid(True)                                 # Adiciona uma grade ao fundo do gráfico

# 4. Exibir o gráfico na tela
plt.show()


