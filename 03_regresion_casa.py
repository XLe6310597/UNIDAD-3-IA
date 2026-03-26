from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([60, 65, 70, 80, 90])

modelo = LinearRegression()
modelo.fit(X, y)

prediccion = modelo.predict([[6]])

print("Calificación estimada para 6 horas de estudio:", prediccion[0])