# ---------------- IMPORTS PRINCIPAIS ----------------
import random                   # Para gerar números aleatórios
import math                     # Funções matemáticas
from collections import Counter # Contagem de elementos
import numpy as np              # Biblioteca científica para arrays e cálculos
import matplotlib.pyplot as plt # Para gráficos

# ---------------- BIBLIOTECAS DE CIÊNCIA DE DADOS / IA ----------------
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import roc_curve, auc

# ---------------- BIBLIOTECAS CIENTÍFICAS ----------------
from scipy import stats
from scipy import integrate

# ---------------- REPRODUTIBILIDADE ----------------
random.seed(42)   # Garante que a aleatoriedade seja a mesma em cada execução
np.random.seed(42)

# ---------------- EXEMPLO 1: URNA DE BOLAS ----------------
urna = ["vermelha"] * 3 + ["azul"] * 2  # 3 bolas vermelhas e 2 azuis

# 1) Probabilidade teórica de tirar uma bola vermelha
p_teorica = 3 / 5

# 2) Probabilidade experimental via simulação
n = 10_000  # número de sorteios
sorteios = [random.choice(urna) for _ in range(n)]  # sorteia aleatoriamente n vezes
p_exp = sorteios.count("vermelha") / n             # calcula a frequência relativa

# Exibe os resultados
print(f"Probabilidade teórica (vermelha): {p_teorica:.4f}")
print(f"Probabilidade experimental (vermelha): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")

# ---------------- EXEMPLO 2: LANCAMENTO DE DADO ----------------
lados = [1,2,3,4,5,6]      # lados do dado
p_teorica = 3 / 6           # probabilidade teórica de sair número par {2,4,6}

# Simulação de lançamentos
N = 100_000  # número de lançamentos
rolagens = np.random.choice(lados, size=N, replace=True)  # gera N números aleatórios
p_exp = np.isin(rolagens, [2,4,6]).mean()                # frequência relativa de números pares

# Exibe os resultados
print(f"Probabilidade teórica (par): {p_teorica:.4f}")
print(f"Probabilidade experimental (par): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")
