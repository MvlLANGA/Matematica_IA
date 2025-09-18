import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Criando dados simples
dados ={
    "Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
    "Idade": [23,31,29,35,28],
    "Salario": [2500, 4000, 3700, 5200, 3300],
    "Departamento": ["TI", "RH", "TI", "Financeiro", "RH"]
}

df= pd.DataFrame(dados)
print(df)
print("-"*40)

#Ver primeiras linhas
print(df.head())
print("-"*40)

#Estatisticas descritivas (média, desvio padrão, etc)
print(df.describe())
print("-"*30)

#Filtrar pessoas com salarios acima de 3500
print(df["Salario"] > 3500)
print("-"*30)

#agrupar por departamento e calcular média salarial
print(df.groupby("Departamento")["Salario"].mean())
print("-"*30)

#Usando o matplotlib e seaborn
#Histograma da idade
sns.histplot(df["Idade"], kde=True, color="orange") #histoplot mostra a distribuição de uma variavel numerica
plt.title("Distribuição de Idades")
plt.show()

#Boxplot do salario do departamento
sns.boxplot(x="Departamento", y="Salario", data=df, color="green") #Boxplot é otimo para ver mediana, quartis e outiliers.
plt.title("Salario por Departamento")
plt.show()

#Grafico de barras da média salarial por departamento
sns.barplot(x="Departamento", y="Salario", data=df, color="brown", estimator="mean") # barplot compara categorias com base em médias (ou outra métrica)
plt.title("Média salarial por Departamento")
plt.show()

# Usando o Scatterplot para ver a s relações entre duas variaveis numericas
sns.scatterplot(x="Idade", y="Salario", hue="Departamento",  data=df)
plt.title("Idade x Salario")
plt.show()