import numpy as np
import random 

# CONFIGURAÇÃO 
# Temos uma urna com 5 bolas: 3 vermelhas (R) e 2 azuis (B)
bolas = ['R','R','R','B','B']
# Número de simulações
n_sim = 10000

# Lista para armazenar os resultados de cada sorteio
resultados = []

# SIMULAÇÃO 
for _ in range(n_sim):
    np.random.shuffle(bolas)
    sorteio = bolas[0]
    resultados.append(sorteio)
resultados = np.array(resultados)

# EVENTOS
A = resultados == 'R'
B = np.arange(n_sim) % 2 == 1

# PROBABILIDADE 
P_sim = np.mean(A | B)
print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")