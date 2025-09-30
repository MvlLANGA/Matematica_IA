# Importa a biblioteca pandas, que é usada para manipulação e análise de dados.
import pandas as pd 

# Lê os dados do arquivo CSV chamado "dados1.csv" e armazena no DataFrame chamado df.
df = pd.read_csv("dados1.csv")

# Agrupa os dados por três colunas: "Companhia", "Aeroporto Origem" e "Aeroporto Destino".
# Em seguida, aplica agregações (funções de resumo) para as colunas numéricas:
# - Soma os valores da coluna "Passageiros"
# - Soma os valores da coluna "Receita (R$)"
# - Calcula a média dos valores da coluna "Ocupação (%)"
# O resultado é um novo DataFrame chamado 'grouped'.
grouped = df.groupby(["Companhia", "Aeroporto Origem", "Aeroporto Destino"]).agg({
    "Passageiros": "sum",            # Soma total de passageiros por rota
    "Receita (R$)": "sum",           # Soma total da receita por rota
    "Ocupação (%)": "mean"           # Média da ocupação dos voos por rota
}).reset_index()                     # Reseta os índices para transformar os grupos em colunas

# Exibe uma mensagem indicando que o novo DataFrame agrupado será mostrado.
print("O FORMATO DO NOVO DATAFRAME APÓS O AGRUPAMENTO!!")

# Imprime o DataFrame 'grouped' que contém os dados agregados por rota
print(grouped)

# Cria uma nova coluna chamada "Receita por Passageiro".
# Essa coluna é calculada dividindo a receita total pela quantidade total de passageiros.
# Essa métrica mostra quanto, em média, foi arrecadado por cada passageiro em uma rota.
grouped['Receita por Passageiro'] = grouped['Receita (R$)'] / grouped['Passageiros']

# Ordena o DataFrame 'grouped' com base na coluna "Receita por Passageiro" em ordem decrescente.
# As rotas com maior receita por passageiro ficarão no topo.
melhores_rotas = grouped.sort_values(by='Receita por Passageiro', ascending=False)

# Exibe uma mensagem indicando que serão mostradas as 5 melhores rotas.
print("AS CINCO MELHORES ROTAS ORDENADAS POR RECEITA POR PASSAGEIRO SÃO:")

# Mostra as 5 primeiras linhas do DataFrame 'melhores_rotas',
# que representam as 5 rotas mais rentáveis por passageiro.
print(melhores_rotas.head())
