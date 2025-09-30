import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("dados1.csv")
print("")
print("---Fazendo a leitura das 5 primeiras linhas do csv.---")
print(df.head())
print("-"*30)

print("---Verificando numero de Linhas/Colunas e tipos de dados---")
linhas_colunas= df.info()
print(linhas_colunas)
print("-"*30)

print("---Fazendo a leitura de valores nulos.---")
valores_nulos= df.isnull().sum()
print(valores_nulos)
print("-"*30)

print("---Calculando a Média, Mediana, Desvio-Padrão e variancia.--- ")
media = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].mean().reset_index()
print(media)
print("-"*30)

print("---Calculando a Mediana---")
mediana = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].median().reset_index()
print(mediana)
print("-"*30)

print("---Calculando o Desvio padrão---")
desvio_padrao=df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].std().reset_index()
print(desvio_padrao)
print("-"*30)

print("---Calculando a Variança.---")
varianca = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].var().reset_index()
print(varianca)
print("-"*30)

print("Calculando o Percentil 25%, 50% e 75%")
percentis = np.percentile(df["Receita (R$)"], [25, 50, 75])
print(f"Percentil 25: {percentis[0]}")
print(f"Percentil 50: {percentis[1]}")  
print(f"Percentil 75: {percentis[2]}")
print("-"*30)



df_agrupado = df.groupby('Companhia').agg({
    'Passageiros': 'sum',
    'Receita (R$)': 'sum'
}).reset_index()


df_ordenado_receita = df_agrupado.sort_values(by='Receita (R$)', ascending=False)
print("---Companhia com maior receita---")
print(df_ordenado_receita)
print("-"*30)


df_ordenado_passageiros = df_agrupado.sort_values(by='Passageiros', ascending=False)
print(df_ordenado_passageiros)
print("-"*30)

print("---Contagem de voos por companhia---")
voos_por_companhia = df['Companhia'].value_counts().reset_index()
voos_por_companhia.columns = ['Companhia', 'Quantidade de Voos']
print(voos_por_companhia)
print("-"*30)


receita_media = df.groupby(['Companhia', 'Aeroporto Origem'])['Receita (R$)'].mean().reset_index()
receita_media.rename(columns={'Receita (R$)': 'Receita Média (R$)'}, inplace=True)
print("---Receita média por companhia e por aeroporto de origem---")
print(receita_media)
print("-"*30)

voos_por_aeroporto = df['Aeroporto Origem'].value_counts().reset_index()
voos_por_aeroporto.columns = ['Aeroporto Origem', 'Quantidade de Voos']
print(voos_por_aeroporto.head(10))

df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.to_period('M').astype(str)
receita_media_mes = df.groupby('Mês')['Receita (R$)'].mean().reset_index()
receita_media_mes.rename(columns={'Receita (R$)': 'Receita Média (R$)'}, inplace=True)

print("---Receita média por mês---")
print(receita_media_mes)
print("-" * 30)


ocupacao_media = df.groupby('Companhia')['Ocupação (%)'].mean().reset_index()
ocupacao_media.rename(columns={'Ocupação (%)': 'Ocupação Média (%)'}, inplace=True)
print("---Ocupação média por companhia---")
print(ocupacao_media)
print("-" * 30)


df['Rota'] = df['Aeroporto Origem'] + " → " + df['Aeroporto Destino']
ocupacao_rota = df.groupby(['Companhia', 'Rota'])['Ocupação (%)'].mean().reset_index()
ocupacao_rota_ordenado = ocupacao_rota.sort_values(by='Ocupação (%)', ascending=False)
print("---Top 5 rotas mais eficientes por Ocupação Média---")
print(ocupacao_rota_ordenado.head(5))
print("-" * 30)


df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.to_period('M').astype(str)
passageiros_mensal = df.groupby(['Companhia', 'Mês'])['Passageiros'].sum().reset_index()
print("---Evolução mensal do total de passageiros por companhia---")
print(passageiros_mensal.head())
print("-" * 30)



plt.figure()
sns.histplot(df["Passageiros"], kde=True, bins=10, color='green')
plt.title("Passageiros")
plt.show()

plt.figure()
sns.boxplot(x="Ocupação (%)", y="Companhia", data=df, color="orange") 
plt.title("Ocupação x Companhia Aerea")
plt.show()

plt.figure()
sns.barplot(x="Receita (R$)", y="Companhia", data=df, color="brown", estimator="mean") 
plt.title("Receita Média x Companhia Aerea")
plt.show()

plt.figure()
sns.scatterplot(x="Distância (km)", y="Receita (R$)", hue="Companhia",  data=df)
plt.title("Distância x Receita")
plt.show()

plt.figure()
sns.heatmap(df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa entre variaveis")
plt.show()

sns.barplot(data=receita_media, x='Aeroporto Origem', y='Receita Média (R$)', hue='Companhia')
plt.title('Receita Média por Companhia e Aeroporto de Origem')
plt.xlabel('Aeroporto de Origem')
plt.ylabel('Receita Média (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))  
sns.barplot(data=ocupacao_media, x='Companhia', y='Ocupação Média (%)', palette='viridis')
plt.title('Ocupação Média (%) por Companhia')
plt.xlabel('Companhia')                        
plt.ylabel('Ocupação Média (%)')              
plt.xticks(rotation=45)  
plt.tight_layout()      
plt.show() 


plt.figure(figsize=(14, 6))
sns.lineplot(data=passageiros_mensal, x='Mês', y='Passageiros', hue='Companhia', marker='o')
plt.title('Evolução Mensal do Total de Passageiros por Companhia')
plt.xlabel('Mês')
plt.ylabel('Número de Passageiros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()