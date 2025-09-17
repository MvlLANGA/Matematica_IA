import numpy as np

numeros = [12,15,12,18,20,15,22,19,15,10]

Q1 = np.percentile(numeros,25)
Q2 = np.percentile(numeros, 50)
Q3 = np.percentile(numeros,75)

print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")