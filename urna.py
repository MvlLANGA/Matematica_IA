import numpy as np

# ---------------- CONFIGURAÇÃO ----------------
# Temos uma urna com 5 bolas: 3 vermelhas (R) e 2 azuis (B)
bolas = ['R','R','R','B','B']

# Número de simulações
n_sim = 10000

# Lista para armazenar os resultados de cada sorteio
resultados = []

# ---------------- SIMULAÇÃO ----------------
for _ in range(n_sim):
    # Embaralha as bolas
    np.random.shuffle(bolas)
    # Pega a primeira bola do embaralhamento (como se fosse um sorteio)
    sorteio = bolas[0]
    resultados.append(sorteio)

# Converte resultados para um array NumPy para facilitar operações
resultados = np.array(resultados)

# ---------------- EVENTOS ----------------
# Evento A: a bola sorteada é vermelha (R)
A = resultados == 'R'

# Evento B: o índice da simulação é ímpar
# np.arange(n_sim) gera [0,1,2,...,9999]
# "% 2 == 1" marca os índices ímpares como True
B = np.arange(n_sim) % 2 == 1

# ---------------- PROBABILIDADE ----------------
# A | B significa "A OU B" (ocorre A ou ocorre B)
# np.mean() calcula a proporção de vezes em que isso é verdadeiro
P_sim = np.mean(A | B)

# Exibe a probabilidade simulada
print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")

