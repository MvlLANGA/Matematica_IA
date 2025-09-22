# Importa a biblioteca matplotlib para plotar gráficos
import matplotlib.pyplot as plt

# Importa a biblioteca numpy para cálculos numéricos e geração de arrays
import numpy as np

# Cria um array de 100 valores igualmente espaçados entre 0 e 10
x = np.linspace(0, 10, 100)

#Primeiro Gráfico: Seno
# Cria uma nova figura (janela de gráfico)
plt.figure()

# Plota a função seno de x
plt.plot(x, np.sin(x))

# Adiciona o título ao gráfico
plt.title("Seno")

# Exibe a figura sem bloquear a execução do código
plt.show(block=False)

#Segundo Gráfico: Cosseno
# Cria uma nova figura para o segundo gráfico
plt.figure()

# Plota a função cosseno de x
plt.plot(x, np.cos(x))

# Adiciona o título ao gráfico
plt.title("Cosseno")

# Exibe a figura sem bloquear a execução do código
plt.show(block=False)

#Terceiro Gráfico: Tangente

# Cria uma nova figura par o terceiro gráfico
plt.figure()

# Plota a função tangente de x
plt.plot(x, np.tan(x))

# Limita o eixo y para evitar valores muito altos (a tangente tende ao infinito)
plt.ylim(-10, 10)

# Adiciona o título ao gráfico
plt.title("Tangente")

# Exibe a figura sem bloquear a execução do código
plt.show(block=False)

# ---------------------- Espera do usuário ----------------------

# Mantém os gráficos abertos até que o usuário pressione Enter
input("Pressione Enter para fechar tudo...")

# Fecha todas as janelas de gráficos abertas
plt.close('all')
