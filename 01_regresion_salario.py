from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de entrada
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([8000, 10000, 12000, 14000, 16000])

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción
prediccion = modelo.predict([[6]])

print("Predicción de salario para 6 años de experiencia:", prediccion[0])