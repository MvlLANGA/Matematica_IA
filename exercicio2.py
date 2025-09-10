import numpy as np
from scipy import stats



print('')
notas_iniciais = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]

media_inicial = np.mean(notas_iniciais) #Calcula a media
desvio_inicial = np.std(notas_iniciais, ddof=1)  # ddof=1 para amostral
print("Média inicial:", media_inicial)
print("Desvio padrão inicial:", desvio_inicial)

# Teste t (H0: média = 70)
t_stat, p_valor = stats.ttest_1samp(notas_iniciais, popmean=75) #Faz um teste para verficar se a média de amostra é estatisticamente diferente de um valor especifico
#No popmean nos criamos uma hipotese. No caso criamos uma meida de notas
print("t =", t_stat, "p =", p_valor)
