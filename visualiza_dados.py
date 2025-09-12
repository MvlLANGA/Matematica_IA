# Importa os pacotes necessários
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- LEITURA DO CSV ----------------
# Lê o arquivo CSV que contém os dados.
# Espera-se que esse arquivo tenha uma coluna chamada 'valor'.
df = pd.read_csv('dados_skew_kurtosis.csv')

# ---------------- CONFIGURAÇÃO DA FIGURA ----------------
# Cria uma figura com tamanho definido (14 de largura x 6 de altura).
plt.figure(figsize=(14, 6))

# ---------------- HISTOGRAMA ----------------
# Cria o primeiro subplot: 1 linha, 2 colunas, posição 1.
plt.subplot(1, 2, 1)

# Plota o histograma da coluna 'valor'.
# - bins=50 → número de barras do histograma
# - kde=True → adiciona a curva de densidade suavizada (Kernel Density Estimate)
# - color → define a cor das barras
sns.histplot(df['valor'], bins=50, kde=True, color='skyblue')

# Define título e rótulos do eixo X e Y
plt.title('Histograma com KDE (Distribuição dos Dados)')
plt.xlabel('Valor')
plt.ylabel('Frequência')

# ---------------- BOXPLOT ----------------
# Cria o segundo subplot: 1 linha, 2 colunas, posição 2.
plt.subplot(1, 2, 2)

# Plota o boxplot da coluna 'valor'.
# O boxplot mostra mediana, quartis e outliers.
sns.boxplot(x=df['valor'], color='lightgreen')

# Define o título do gráfico
plt.title('Boxplot dos Dados')

# ---------------- AJUSTE FINAL ----------------
# Ajusta automaticamente o espaçamento dos gráficos
# para que os títulos e rótulos não fiquem sobrepostos.
plt.tight_layout()

# Exibe os gráficos na tela.
plt.show()
