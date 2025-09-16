import numpy as np

bolas = ['R','R','R','B','B']
n_sim = 10000
resultados = []

# SIMULAÇÃO 
for _ in range(n_sim):
    np.random.shuffle(bolas)
    sorteio = bolas[0]
    resultados.append(sorteio)

resultados = np.array(resultados)
A = resultados == 'B'
B = np.arange(n_sim) %5 == 0
P_sim = np.mean(A | B)


print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")