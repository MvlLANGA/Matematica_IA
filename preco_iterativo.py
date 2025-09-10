# ----------------------
# 1) Importação de bibliotecas
# ----------------------
import pandas as pd                # Manipulação de tabelas (DataFrames) e leitura de CSV
import matplotlib.pyplot as plt    # Plotagem de gráficos
from sklearn.linear_model import LinearRegression   # Regressão linear
from sklearn.preprocessing import PolynomialFeatures # Criação de termos polinomiais
import numpy as np                 # Operações numéricas
from sklearn.metrics import r2_score, mean_squared_error # Métricas de avaliação

# ----------------------
# 2) Leitura do dataset
# ----------------------
# O arquivo area_preco.csv deve conter pelo menos duas colunas: 'Area' e 'Preco'.
#   - 'Area' representa a metragem (m²).
#   - 'Preco' representa o valor associado (R$).
#
# O pandas cria um DataFrame com esses dados para manipulação.
dados = pd.read_csv('area_preco.csv')
X = dados[['Area']]  # X deve ser bidimensional, por isso usamos [[ ]]
y = dados['Preco']   # y é o alvo (preço)

# ----------------------
# 3) Visualização inicial dos dados
# ----------------------
# O gráfico de dispersão mostra a relação entre área e preço.
plt.figure(figsize=(8, 6))   # Define o tamanho do gráfico
plt.scatter(X, y, color='blue', label='Dados reais')

# ----------------------
# 4) Teste de diferentes graus polinomiais
# ----------------------
# graus: lista com os graus de polinômio que serão testados
# cores: cores correspondentes a cada curva para diferenciar no gráfico
graus = [1, 2, 3, 4]
cores = ['red', 'green', 'orange', 'purple']

for grau, cor in zip(graus, cores):
    # Criação de termos polinomiais (ex.: grau=2 -> [1, x, x²])
    poly = PolynomialFeatures(degree=grau)
    X_poly = poly.fit_transform(X)

    # Ajuste do modelo de regressão
    modelo = LinearRegression()
    modelo.fit(X_poly, y)

    # Predição dos valores estimados
    y_previsto = modelo.predict(X_poly)

    # Ordenar os valores de X para que a linha seja plotada de forma contínua
    sort_idx = np.argsort(X.values.flatten())

    # Desenhar a curva correspondente ao grau
    plt.plot(
        X.values.flatten()[sort_idx],     # Área ordenada
        y_previsto[sort_idx],             # Preço previsto ordenado
        color=cor,
        linestyle='--' if grau > 1 else '-', # Linha pontilhada para polinomiais > 1
        label=f'Polinomial grau {grau} (R²={r2_score(y, y_previsto):.3f})' # R² na legenda
    )

# ----------------------
# 5) Ajustes do gráfico
# ----------------------
plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.title('Comparação de Regressões Polinomiais')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------
# Observações finais
# ----------------------
# - O R² (coeficiente de determinação) indica o quanto o modelo explica da variação dos dados.
# - Um grau mais alto tende a ajustar melhor os pontos de treino, mas pode causar overfitting.
# - Para avaliar melhor, pode-se separar dados de treino e teste.
# - RMSE ou MAE também são úteis para medir erro médio das previsões.