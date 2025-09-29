import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o arquivo CSV com os dados do dataset
df = pd.read_csv("dados1.csv")

print("")
print("---Fazendo a leitura das 5 primeiras linhas do csv.---")
print(df.head())  # Exibe as primeiras 5 linhas para termos uma ideia inicial dos dados: colunas, tipos e alguns valores
print("-" * 30)

print("---Verificando numero de Linhas/Colunas e tipos de dados---")
linhas_colunas = df.info()  # Exibe a quantidade de linhas, colunas, nomes das colunas e o tipo de dados de cada coluna
print(linhas_colunas)
print("-" * 30)

print("---Fazendo a leitura de valores nulos.---")
# Checa se existem valores faltantes/nulos em cada coluna, pois isso pode afetar análises futuras
valores_nulos = df.isnull().sum()
print(valores_nulos)
print("-" * 30)

print("---Calculando a Média, Mediana, Desvio-Padrão e variancia.--- ")
# Calcula a média para as colunas selecionadas (números que representam passageiros, distância, ocupação e receita)
media = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].mean().reset_index()
print(media)
print("-" * 30)

print("---Calculando a Mediana---")
# Calcula a mediana, que é o valor central quando os dados são ordenados, para as mesmas colunas
mediana = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].median().reset_index()
print(mediana)
print("-" * 30)

print("---Calculando o Desvio padrão---")
# Calcula o desvio padrão, que indica o quanto os dados variam em torno da média
desvio_padrao = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].std().reset_index()
print(desvio_padrao)
print("-" * 30)

print("---Calculando a Variança.---")
# Calcula a variância, que é o quadrado do desvio padrão e também indica dispersão dos dados
varianca = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].var().reset_index()
print(varianca)
print("-" * 30)

print("Calculando o Percentil 25%, 50% e 75%")
# Calcula os percentis 25, 50 (mediana) e 75 da receita, que indicam valores abaixo dos quais se encontram 25%, 50% e 75% dos dados
percentis = np.percentile(df["Receita (R$)"], [25, 50, 75])
print(f"Percentil 25: {percentis[0]}")
print(f"Percentil 50: {percentis[1]}")  # Mediana
print(f"Percentil 75: {percentis[2]}")
print("-" * 30)

# Agrupa o dataframe pela coluna 'Companhia' somando o total de passageiros e receita para cada companhia aérea
df_agrupado = df.groupby('Companhia').agg({
    'Passageiros': 'sum',
    'Receita (R$)': 'sum'
}).reset_index()

# Ordena o dataframe agrupado por receita total em ordem decrescente para saber qual companhia gerou mais receita
df_ordenado_receita = df_agrupado.sort_values(by='Receita (R$)', ascending=False)
print("---Companhia com maior receita---")
print(df_ordenado_receita)
print("-" * 30)

# Ordena o dataframe agrupado por total de passageiros em ordem decrescente para saber qual companhia transportou mais pessoas
df_ordenado_passageiros = df_agrupado.sort_values(by='Passageiros', ascending=False)
print(df_ordenado_passageiros)
print("-" * 30)

print("---Contagem de voos por companhia---")
# Conta o número de ocorrências (voos) para cada companhia, mostrando quantos voos cada uma fez
voos_por_companhia = df['Companhia'].value_counts().reset_index()
voos_por_companhia.columns = ['Companhia', 'Quantidade de Voos']
print(voos_por_companhia)
print("-" * 30)

# Agrupa dados por companhia e aeroporto de origem para calcular a receita média gerada por cada combinação
receita_media = df.groupby(['Companhia', 'Aeroporto Origem'])['Receita (R$)'].mean().reset_index()
# Renomeia a coluna para melhor entendimento
receita_media.rename(columns={'Receita (R$)': 'Receita Média (R$)'}, inplace=True)
print("---Receita média por companhia e por aeroporto de origem---")
print(receita_media)
print("-" * 30)

# Conta quantos voos saíram de cada aeroporto de origem
voos_por_aeroporto = df['Aeroporto Origem'].value_counts().reset_index()
voos_por_aeroporto.columns = ['Aeroporto Origem', 'Quantidade de Voos']
print(voos_por_aeroporto.head(10))  # Mostra os 10 aeroportos com mais voos
print("-" * 30)

# Converte a coluna 'Data' para o tipo datetime para facilitar análises temporais posteriores
df['Data'] = pd.to_datetime(df['Data'])

# Cria uma nova coluna 'Mês' no formato ano-mês (YYYY-MM), usando apenas a parte do mês da data
df['Mês'] = df['Data'].dt.to_period('M').astype(str)

# Agrupa os dados por mês para calcular a receita média mensal geral (todas as companhias juntas)
receita_media_mes = df.groupby('Mês')['Receita (R$)'].mean().reset_index()
receita_media_mes.rename(columns={'Receita (R$)': 'Receita Média (R$)'}, inplace=True)

print("---Receita média por mês---")
print(receita_media_mes)
print("-" * 30)

# Agrupa os dados por companhia para calcular a ocupação média (em %) de cada companhia aérea
ocupacao_media = df.groupby('Companhia')['Ocupação (%)'].mean().reset_index()
ocupacao_media.rename(columns={'Ocupação (%)': 'Ocupação Média (%)'}, inplace=True)
print("---Ocupação média por companhia---")
print(ocupacao_media)
print("-" * 30)

# Cria uma nova coluna 'Rota', que concatena o aeroporto de origem e destino no formato "Origem → Destino"
df['Rota'] = df['Aeroporto Origem'] + " → " + df['Aeroporto Destino']

# Agrupa os dados por companhia e rota para calcular a ocupação média em cada rota para cada companhia
ocupacao_rota = df.groupby(['Companhia', 'Rota'])['Ocupação (%)'].mean().reset_index()

# Ordena as rotas por ocupação média em ordem decrescente, para identificar as rotas mais eficientes (mais ocupadas)
ocupacao_rota_ordenado = ocupacao_rota.sort_values(by='Ocupação (%)', ascending=False)
print("---Top 5 rotas mais eficientes por Ocupação Média---")
print(ocupacao_rota_ordenado.head(5))  # Exibe as 5 rotas mais eficientes
print("-" * 30)

# Garantindo novamente que a coluna 'Data' está no formato datetime, para evitar erros (mesmo passo feito antes)
df['Data'] = pd.to_datetime(df['Data'])

# Criando novamente a coluna 'Mês' para análise temporal (por segurança, evita perda da coluna)
df['Mês'] = df['Data'].dt.to_period('M').astype(str)

# Agrupa os dados por companhia e mês para calcular o total de passageiros transportados mensalmente por cada companhia
passageiros_mensal = df.groupby(['Companhia', 'Mês'])['Passageiros'].sum().reset_index()

print("---Evolução mensal do total de passageiros por companhia---")
print(passageiros_mensal.head())  # Exibe as primeiras linhas da tabela de evolução mensal
print("-" * 30)

# --- Visualizações gráficas ---

# Histograma com KDE para analisar a distribuição do número de passageiros nos voos
plt.figure()
sns.histplot(df["Passageiros"], kde=True, bins=10, color='green')
plt.title("Passageiros")
plt.show()

# Boxplot para visualizar a distribuição da ocupação percentual por companhia aérea, facilitando comparação entre elas
plt.figure()
sns.boxplot(x="Ocupação (%)", y="Companhia", data=df, color="orange")
plt.title("Ocupação x Companhia Aerea")
plt.show()

# Gráfico de barras mostrando a receita média por companhia, facilita ver quem tem maior receita média por voo
plt.figure()
sns.barplot(x="Receita (R$)", y="Companhia", data=df, color="brown", estimator="mean")
plt.title("Receita Média x Companhia Aerea")
plt.show()

# Scatterplot que relaciona a distância do voo e a receita gerada, colorido por companhia para analisar padrões
plt.figure()
sns.scatterplot(x="Distância (km)", y="Receita (R$)", hue="Companhia", data=df)
plt.title("Distância x Receita")
plt.show()
# Heatmap mostrando a correlação entre as variáveis numéricas principais

# Define o tamanho da figura para melhor visualização
plt.figure(figsize=(14, 7))
# Gráfico de barras agrupado: eixo x = Aeroporto Origem, y = Receita Média, com barras para cada Companhia
sns.barplot(data=receita_media, x='Aeroporto Origem', y='Receita Média (R$)', hue='Companhia')
# Adiciona título e rótulos
plt.title('Receita Média por Companhia e Aeroporto de Origem')
plt.xlabel('Aeroporto de Origem')
plt.ylabel('Receita Média (R$)')
# Rotaciona os rótulos do eixo x para melhor leitura (caso sejam muitos e/ou grandes)
plt.xticks(rotation=45)
# Ajusta layout para não cortar nada
plt.tight_layout()
# Exibe o gráfico
plt.show()

plt.figure(figsize=(10, 6))  # Define o tamanho da figura
# Gráfico de barras: eixo x = Companhia, y = Ocupação Média (%)
sns.barplot(data=ocupacao_media, x='Companhia', y='Ocupação Média (%)', palette='viridis')
plt.title('Ocupação Média (%) por Companhia')  # Título do gráfico
plt.xlabel('Companhia')                        # Rótulo do eixo x
plt.ylabel('Ocupação Média (%)')               # Rótulo do eixo y
plt.xticks(rotation=45)  # Rotaciona os nomes das companhias para melhor leitura
plt.tight_layout()       # Ajusta o layout para não cortar nada
plt.show()               # Exibe o gráfico

# Heatmap mostrando a correlação entre as variáveis numéricas principais
