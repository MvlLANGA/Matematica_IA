import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

# ---------------- CONFIGURAÇÃO ----------------
# Define a semente do gerador aleatório para reprodutibilidade.
# Assim, sempre que rodar, os números serão os mesmos.
np.random.seed(42)

# ---------------- GERAÇÃO DE DADOS ----------------
# Gera 1000 valores com distribuição normal (média=2, desvio padrão=0.2).
# Como a variância é baixa, os valores ficam bem concentrados em torno de 2.
dados_normais = np.random.normal(loc=2, scale=0.2, size=1000)

# Gera 20 valores com distribuição exponencial (cauda longa à direita).
# Esses valores funcionam como "outliers positivos", criando assimetria.
outliers = np.random.exponential(scale=10, size=20)

# Combina os dois conjuntos (normais + outliers).
dados_com_outliers = np.concatenate([dados_normais, outliers])

# ---------------- DATAFRAME ----------------
# Cria um DataFrame para organizar os dados em duas colunas:
# - id: número sequencial de 1 até o total de elementos
# - valor: os números gerados
df = pd.DataFrame({
    'id': range(1, len(dados_com_outliers) + 1),
    'valor': dados_com_outliers
})

# ---------------- ESTATÍSTICAS ----------------
# Calcula a assimetria (skewness): 
# valores > 0 indicam cauda à direita (assimetria positiva).
skew_val = skew(dados_com_outliers)

# Calcula a curtose (kurtosis):
# valores > 0 indicam caudas mais pesadas que a normal.
kurt_val = kurtosis(dados_com_outliers)

print('')
print("Skewness:", skew_val)
print("-"*30)
print("Kurtosis:", kurt_val)
print('')

# ---------------- EXPORTAÇÃO ----------------
# Salva os dados no arquivo CSV (sem incluir o índice automático do pandas).
df.to_csv("dados_skew_kurtosis.csv", index=False)
print("Arquivo 'dados_skew_kurtosis.csv' criado com sucesso!")
