import random #fornece funções para gerar numeros aleatórios.

#Nesse coidigo, ele será usado para simular lançamentos de dados.

# ---------------- PROBABILIDADE TEÓRICA ----------------
# Lista com os números pares do dado (2, 4, 6)
pares = [x for x in range(1, 7) if x % 2 == 0]

# Probabilidade teórica: quantidade de pares / total de lados do dado
prob_teorica = len(pares) / 6   # 3/6 = 0.5 o len calcula o tamanho no caso 2, 4 e 6 os pares.

# ---------------- SIMULAÇÃO ----------------
# Faz 10.000 lançamentos de um dado (números de 1 a 6)
simulacoes = [random.randint(1, 6) for _ in range(10000)]

# Frequência relativa: proporção de vezes que saiu par
freq_par = sum(1 for x in simulacoes if x % 2 == 0) / len(simulacoes) # O sum ele vai somar se cada vez que o dado cair em um numero que seja divisivel por 2 e a sobra é igual a zero ele conta para o par se for ao contrario ele vai contar para o impar e após rodar 10000 vezes ele faz a soma e porcentagem de cada um.

# ---------------- RESULTADOS ----------------
print(f"Probabilidade: Teórica: {prob_teorica}, Simulada: {freq_par}")

