#Média movel
# Importa a biblioteca seaborn para visualizações estatísticas
import seaborn as sns

# Importa a biblioteca matplotlib.pyplot para exibição de gráficos
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
# Gera 100 números aleatórios seguindo uma distribuição normal
# loc=50 define a média como 50
# scale=10 define o desvio padrão como 10
# size=100 define a quantidade de dados como 100
dados = np.random.normal(loc=50, scale=10, size=100)
 
# Cria um histograma com:
# - kde=True: adiciona uma curva de densidade (KDE)
# - bins=10: define 10 barras (intervalos) no histograma
# - color='orange': define a cor das barras como laranja
sns.histplot(dados, kde=True, bins=10, color='green')

# Define o título do gráfico
plt.title('Histograma com Densidade')

# Exibe o gráfico na tela
plt.show()