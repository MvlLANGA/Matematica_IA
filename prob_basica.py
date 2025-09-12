import random
from collections import Counter

# ---------------- ESPAÇO AMOSTRAL ----------------
# Cria o espaço amostral de todos os pares possíveis (a, b),
# onde cada elemento pode ser 'C' ou 'K'.
# Resultado: [('C','C'), ('C','K'), ('K','C'), ('K','K')]
espaco_amostral = [(a,b) for a in ['C','K'] for b in ['C','K']]
print("Espaço amostral:", espaco_amostral)

# ---------------- SIMULAÇÃO ----------------
# Gera 10.000 resultados simulados escolhendo aleatoriamente 'C' ou 'K' para cada posição do par.
# Exemplo de saída: ('C','K'), ('K','K'), etc.
resultados = [(random.choice(['C','K']), random.choice(['C','K'])) for _ in range(10000)]

# ---------------- FREQUÊNCIAS ----------------
# Conta quantas vezes cada par apareceu na simulação.
# Counter cria um dicionário do tipo: {('C','C'): qtd, ('C','K'): qtd, ...}
frequencias = Counter(resultados)

# Mostra o número de vezes que cada combinação ocorreu
print(frequencias)
