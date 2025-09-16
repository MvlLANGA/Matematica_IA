import numpy as np

# Temos 5 bolas: 3 vermelhas (R) e 2 azuis (B)
bolas = np.array(["R", "R", "R", "B", "B"])
n_sim = 10000  # número de simulações

# Sorteamos 3 bolas em cada simulação, com reposição
# Ou seja, cada sorteio é independente, sempre voltam as bolas
sorteios = np.random.choice(bolas, size=(n_sim, 3), replace=True)

# Evento: todas as 3 bolas sorteadas são vermelhas
a = np.all(sorteios == "R", axis=1) # O axis=1 ele opera nas colunas da esquerda para direita
# Se fosse axis=0 seria nas colunas de cima para baixo

# Probabilidade estimada via simulação
p_sim = np.mean(a)

print(f"Probabilidade de 3 vermelhas em sequência (com reposição) ~ {p_sim:.2f}")
