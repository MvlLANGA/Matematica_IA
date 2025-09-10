import numpy as np                   # Biblioteca para cálculos numéricos e arrays
from scipy.stats import pearsonr 
import matplotlib.pyplot as plt   # Função para calcular a correlação de Pearson

# -----------------------------
# Dados de exemplo (horas de sono vs desempenho)
# -----------------------------
horas_dormidas = np.array([4,5,6,7,8,9])   # Horas dormidas por dia
desempenho = np.array([50, 55, 65, 75, 80, 85])  # Desempenho correspondente

# -----------------------------
# Outro exemplo: dados gerados aleatoriamente
# -----------------------------
x = np.random.rand(10)  # 10 números aleatórios entre 0 e 1
y = 2 * x + np.random.normal(0, 0.1, 10)  
# Criamos y como aproximadamente 2*x + ruído gaussiano (média 0, desvio 0.1)

# -----------------------------
# Correlação de Pearson
# -----------------------------
# pearsonr retorna (coeficiente de correlação, p-valor)
correlacao, _ = pearsonr(x, y)

# Mostra o resultado
print("Correlação de Pearson:", correlacao)

plt.scatter(horas_dormidas, desempenho)
plt.plot(horas_dormidas, desempenho, color="orange")
plt.title("Correlação de horas dormidas/desempenho")
plt.xlabel("Horas dormidas")
plt.ylabel("Desempenho")
plt.show()
