import numpy as np
from scipy import stats

# --- Parte 1 ---
print("Parte 1")
print('-'*40)
notas_iniciais = [72, 68, 71, 69, 73, 74, 70, 67, 72, 71]

media_inicial = np.mean(notas_iniciais) #Calcula a media
desvio_inicial = np.std(notas_iniciais, ddof=1)  # ddof=1 para amostral
print("Média inicial:", media_inicial)
print("Desvio padrão inicial:", desvio_inicial)

# Teste t (H0: média = 70)
t_stat, p_valor = stats.ttest_1samp(notas_iniciais, popmean=70) #Faz um teste para verficar se a média de amostra é estatisticamente diferente de um valor especifico
print("t =", t_stat, "p =", p_valor)
print("-"*40)
print("Parte 2")


# --- Parte 2 ---
notas_novas = [75, 78, 77, 74, 76, 79, 80, 81, 77, 76, 78, 75]

media_nova = np.mean(notas_novas)
desvio_novo = np.std(notas_novas, ddof=1)
print("\nMédia nova:", media_nova)
print("Desvio padrão novo:", desvio_novo)

# Teste t (H0: média = 70)
t_stat2, p_valor2 = stats.ttest_1samp(notas_novas, popmean=70) # o valor da media populacional que vice quer comparar com a media da sua amostra. (neste caso, 70)
print("t =", t_stat2, "p =", p_valor2)

# o t precisa estar proximo a 1.
# Enquanto o p precisa estar acima 0.05