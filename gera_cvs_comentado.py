

# Importa as bibliotecas necessárias
import pandas as pd # pandas: manipulação de tabelas (DataFrame), leitura/escrita de CSV, etc.
import numpy as np # numpy: operações numéricas, geração de números aleatórios, arrays


# ----------------------
# 1) Reprodutibilidade
# ----------------------
# np.random.seed fixa a sequência pseudo-aleatória usada pelo numpy. Usar uma semente
# permite que quem rodar o script novamente (ou outro computador) gere exatamente os
# mesmos números aleatórios, o que é útil para debugging e reprodução de resultados.
# A semente '42' é um valor arbitrário (muito comum em exemplos), mas qualquer inteiro é válido.
np.random.seed(42)


# ----------------------
# 2) Geração dos dados
# ----------------------
# Vamos construir um dicionário chamado 'dados', onde cada chave será o nome de uma coluna
# e o valor será um array (ou lista) com o mesmo número de elementos (neste caso 100).
# Usamos np.random.normal para simular variáveis contínuas que seguem uma distribuição
# aproximadamente normal.
#
# np.random.normal(loc, scale, size)
# - loc: média (centro) da distribuição
# - scale: desvio padrão (largura) da distribuição
# - size: número de amostras a gerar


dados = {
# 'idade': média 30 anos, desvio padrão 5 anos, 100 amostras
# Observação: como estamos usando uma normal, alguns valores podem ficar fora do intervalo
# típico (por exemplo < 0). Se isso for um problema, trate com np.clip ou gere com outra distribuição.
"idade": np.random.normal(30, 5, 100),


# 'peso': média 70 kg, desvio padrão 10 kg, 100 amostras
# Dependendo do desvio padrão, pode aparecer peso negativo em casos extremos; trate se necessário.
"peso": np.random.normal(70, 10, 100),


# 'altura': média 1.70 m, desvio padrão 0.1 m, 100 amostras
# Note que altura é em metros aqui (valores como 1.70). Se preferir centímetros, multiplique por 100.
"altura": np.random.normal(1.70, 0.1, 100),
}


# ----------------------
# 3) Criação do DataFrame
# ----------------------
# pandas.DataFrame converte o dicionário em uma tabela (linhas x colunas). O pandas
# infere tipos (provavelmente float64 para essas colunas) e fornece utilitários para
# explorar, transformar e exportar os dados.


df = pd.DataFrame(dados)


# Dicas rápidas (comentadas):
# - df.shape -> (100, 3) : número de linhas e colunas
# - df.dtypes -> mostra os tipos de cada coluna
# - df.head() -> mostra as primeiras linhas
# - df.describe() -> estatísticas descritivas (mean, std, min, max, quartis)
# Exemplo (descomente para usar):
# print(df.shape)
# print(df.dtypes)
# print(df.head())
# print(df.describe())


# ----------------------
# 4) Tratamentos comuns (opcionais)
# ----------------------
# Aqui estão algumas ações comuns que você pode querer executar antes de salvar ou usar
# o dataset em modelagem/visualização. Mantive tudo comentado para não alterar o comportamento
# original do seu script, mas deixei como referência.


# 1) Arredondar valores (ex.: duas casas decimais)
# df['idade'] = df['idade'].round(2)
# df['peso'] = df['peso'].round(2)
# df['altura'] = df['altura'].round(2)


# 2) Evitar valores impossíveis (ex.: idade ou peso negativos)
# df['idade'] = df['idade'].clip(lower=0)
# df['peso'] = df['peso'].clip(lower=0)


# 3) Converter altura para centímetros, se preferir
# df['altura_cm'] = (df['altura'] * 100).round(1)


# 4) Verificar valores faltantes (NaN) — normalmente não ocorrerão com np.random.normal,
# mas é boa prática checar após transformações.
# print(df.isna().sum())


# ----------------------
# 5) Salvar como CSV
# ----------------------
# to_csv grava o DataFrame em um arquivo CSV. index=False evita que o índice do pandas
# (0,1,2,...) seja gravado como coluna extra no CSV.
#
# Observações sobre encoding e compatibilidade com Excel:
# - Por padrão, pandas usa 'utf-8'. No Excel do Windows, às vezes é melhor usar 'utf-8-sig'
# para que o Excel detecte corretamente o BOM e mostre acentuação/acentos sem problemas.
# - Se você precisa de ponto decimal como vírgula (padrão em algumas localidades), trate isso
# depois no Excel ou use parâmetros adicionais ao exportar.


df.to_csv("dataset_exemplo.csv", index=False)


# Mensagem final para indicar que o arquivo foi criado com sucesso
print("✅ Arquivo dataset_exemplo.csv criado!")


# ----------------------
# Observações finais / Sugestões
# ----------------------
# - Se planeja usar este dataset para treinar modelos de ML de classificação, pode adicionar
# uma coluna 'target' (binária ou categórica). Exemplo: df['target'] = np.random.choice([0,1], size=len(df))
# - Para análises exploratórias, use seaborn/matplotlib para visualizar distribuições (histogramas),
# correlações (heatmap) e scatter plots (por exemplo, peso x altura).
# - Se quiser, posso: adicionar uma coluna target, normalizar as features, gerar um conjunto de treino/teste,
# ou salvar o CSV com outra codificação. Me diga o que prefere.