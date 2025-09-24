import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dados_produtos.csv", parse_dates=["Data"])
print(df)

print(df.shape)
print(df.head()) #
print(df.info())


#Fazendo a estatistica descritiva (média, desvio-padrão, quartis)
descrevendo_df= df.describe()
print(descrevendo_df)

receita_total= df["Receita Total"].quantile([0.25,0.5,0.75])
print(receita_total)

#Produto com maior Receita
produto_maior_receita = df.groupby("Produto")["Receita Total"].sum().idxmax()
print("O produto com maior receita: ", produto_maior_receita)
print("-"*30)

#Exibindo a quantidade de registros por produto
registros_produtos = df.value_counts("Produto")
print(registros_produtos)

#Calculando a receita média por regiao
print(df.groupby("Produto")["Receita Total"].mean())

#Fazendo a criação de uma nova coluna (mês)
df['Mes']= df['Data'].dt.to_period('M') #O 'M' vem do ingles Mounth
print(df.head())

#Total de vendas por mes
vendas_mes= df.groupby('Mes')['Vendas'].sum()
print("\n--Vendas por Mes--")
print(vendas_mes)

#calculando a média movel
# Média móvel com janela de 7 períodos
df_sorted = df.sort_values("Data")
df_sorted['MA7']= df_sorted['Receita Total'].rolling(7).mean() #sorted seleciona a coluna dos valores da "Receita total". O rolling cria uma janela móvel de 7 linhas consecutivas(no caso 7 dias aqui)
#O mean calcula a média desses 7 dias dentro de uma janela. 
print(df_sorted)

#Produto mais vendido por Região
# Agrupa por Região e Produto, somando as vendas
vendas_agrupadas = df.groupby(['Região', 'Produto'])['Vendas'].sum().reset_index() # o Reset_index ele organiza a tabela.
print(vendas_agrupadas)

# Para cada região, pega o produto com maior venda
produto_mais_vendido = vendas_agrupadas.sort_values('Vendas', ascending=False).drop_duplicates('Região')

print(produto_mais_vendido)


#Visualização em graficos.

#Histograma
plt.figure()
sns.histplot(df["Vendas"], kde=True, bins=10, color='green')
plt.title("Vendas")
plt.show(block=False)

#Boxplot
plt.figure()
sns.boxplot(x="Receita Total", y="Região", data=df, color="orange") 
plt.title("Receita Total e Região")
plt.show(block=False)

#Grafico de Barras com Receita média por produtos
plt.figure()
sns.barplot(x="Receita Total", y="Produto", data=df, color="brown", estimator="mean") # barplot compara categorias com base em médias (ou outra métrica)
plt.title("Receita média por produto")
plt.show(block=False)

# Usando o Scatterplot para ver as relações entre Vendas e Receita Total
plt.figure()
sns.scatterplot(x="Vendas", y="Receita Total", hue="Produto",  data=df)
plt.title("Vendas x Receita Total")
plt.show(block=False)

plt.figure()
sns.heatmap(df[["Vendas", "Preço Unitário", "Receita Total"]].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de correlação")
plt.show(block=False)

#Total de vendas por mes.
plt.figure(figsize=(7,4))
vendas_mes.plot(kind='line', marker='o')
plt.title("Total de vendas por mes")
plt.xlabel("Dias")
plt.ylabel("Media")
plt.show(block=False)

#Média movel de 7 dias
plt.figure(figsize=(10,5))
plt.plot(df_sorted["Data"], df_sorted["Receita Total"], color="darkgreen", alpha=0.8, label="Receita Diaria")
plt.plot(df_sorted["Data"], df_sorted["MA7"], color="orange", label= "Media movel 7 dias")
plt.legend()
plt.title("Receita Total com média movel(7d)")
plt.show(block=False)

input("Pressione Enter para fechar tudo...")
plt.close('all')