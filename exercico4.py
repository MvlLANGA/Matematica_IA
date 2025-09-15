import numpy as np  # Biblioteca para cálculos numéricos e geração de números aleatórios

# Gerar 5000 lançamentos de um dado honesto
# randint(1, 7, size=5000) → gera inteiros de 1 até 6 (o limite superior 7 não entra)
lancamentos = np.random.randint(1, 7, size=5000)

# Verificar a frequência do número 6
# "lancamentos == 6" cria um array de valores booleanos (True/False)
# Exemplo: [False, True, False, ...] → True quando o valor é 6
# np.mean transforma True=1 e False=0 e calcula a média, ou seja,
# (quantos 6 saíram) ÷ (número total de lançamentos)
prob_estimada = np.mean((lancamentos == 6)|(lancamentos ==5)) # O traço representa Uma coisa (OU) outra não usamos o (OR) e o no lugar do (E) usamos & dai não usamos o (AND) 

# Exibir a probabilidade estimada de sair o número 6
print(f"A probabilidade é: {prob_estimada}")
