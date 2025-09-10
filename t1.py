from scipy import stats
import numpy as np

#aqui nos vamos fazer a comparação entre dois grupos
grupo_A = np.random.normal(70, 10, 30)
grupo_B = np.random.normal(65, 10, 30)

t_stat, p_val = stats.ttest_ind(grupo_A, grupo_B)
print("t =", t_stat , "p-valor =", p_val)

# valor proximo de zero as variaveis são muito parecidas
# p-valor mede a probabilidade dessa diferença e precisa estar perto de 0.05
# E quando o T da um valor muito alto, normalmento o P da um valor muito pequeno.
# E normalmente quando o P for grande o T não sera tão grande.
# resumindo 
# t grande e p pequno = diferença significativa
#t pequeno e p grande = sem evidencia de deiferença
# O t te mostra a intensidade deo efeito, o p te diz se essa intensidade é estatisticamente confiavel.