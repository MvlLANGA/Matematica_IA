import pandas as pd          # Manipulação de dados em DataFrames
import numpy as np           # Operações numéricas e arrays
import matplotlib.pyplot as plt  # Gráficos básicos
import seaborn as sns        # Gráficos mais bonitos e estatísticos
from scipy import stats      # Estatísticas avançadas (skew, kurtosis, moda)

# ---------------- FUNÇÃO PRINCIPAL ----------------
def estatisticas_descritivas(csv_path):
    """
    Função para calcular e visualizar estatísticas descritivas de colunas numéricas de um CSV.
    
    Parâmetros:
        csv_path (str): caminho para o arquivo CSV
        
    Retorna:
        pd.DataFrame: estatísticas descritivas de todas as colunas numéricas
    """
    
    # Carregar dataset
    df = pd.read_csv(csv_path)
    print(f"\n📂 Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.\n")
    
    # Seleciona apenas colunas numéricas
    num_cols = df.select_dtypes(include=np.number).columns
    
    if len(num_cols) == 0:
        print("⚠️ O dataset não possui colunas numéricas para análise.")
        return
    
    resultados = {}  # Dicionário para armazenar estatísticas
    
    # Loop pelas colunas numéricas
    for col in num_cols:
        dados = df[col].dropna()  # Remove valores ausentes (NaN)
        
        # Calcula estatísticas descritivas
        estatisticas = {
            "média": np.mean(dados),
            "mediana": np.median(dados),
            "moda": stats.mode(dados, keepdims=True).mode[0],
            "variância": np.var(dados, ddof=1),       # ddof=1 → variância amostral
            "desvio padrão": np.std(dados, ddof=1),
            "assimetria": stats.skew(dados),          # Skewness (assimetria)
            "curtose": stats.kurtosis(dados)         # Kurtosis (pontiagudez)
        }
        resultados[col] = estatisticas
        
        # Exibe resultados no terminal
        print(f"\n📊 Estatísticas para '{col}':")
        for k, v in estatisticas.items():
            print(f"   {k:15}: {v:.4f}")
        
        # ---------------- VISUALIZAÇÃO ----------------
        plt.figure(figsize=(10,4))
        
        # Histograma com KDE
        plt.subplot(1,2,1)
        sns.histplot(dados, kde=True, bins=20, color="green")
        plt.title(f"Histograma - {col}")
        
        # Boxplot
        plt.subplot(1,2,2)
        sns.boxplot(x=dados, color="orange")
        plt.title(f"Boxplot - {col}")
        
        plt.tight_layout()
        plt.show()
    
    # Retorna DataFrame com todas as estatísticas
    return pd.DataFrame(resultados).T


# ----------------- EXEMPLO DE USO -----------------
estatisticas = estatisticas_descritivas("dataset_exemplo.csv")
print(estatisticas)
