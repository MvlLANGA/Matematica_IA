import statistics  # Biblioteca padrão para estatísticas básicas
import numpy as np  # Biblioteca científica para cálculos numéricos

# ---------------- DADOS ----------------
dados = [10, 20, 20, 30, 40, 50]  # Conjunto de valores

# ---------------- MEDIDAS CENTRAIS ----------------
print("Média:", statistics.mean(dados))       # Média aritmética
print("Mediana:", statistics.median(dados))   # Valor central
print("Moda:", statistics.mode(dados))        # Valor que mais se repete

# ---------------- MEDIDAS DE DISPERSÃO ----------------
print("Desvio padrão:", np.std(dados))       # Quanto os dados se afastam da média
print("Variância:", np.var(dados))           # Quadrado do desvio padrão
