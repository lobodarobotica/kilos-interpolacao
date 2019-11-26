import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[235000], [294000]]) # pesos
y = np.array([0, 50]) # porcentagem

reg = LinearRegression().fit(X, y)

b = reg.intercept_
a = reg.coef_[0] # como só tem uma variável, então seria ax+b (pega indice 0). Se tivesse mais seria a1*x1 + a2*x2 + b

print(a, b)

print(a * 3 + b) # aprox 25