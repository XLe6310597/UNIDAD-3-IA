from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[50], [60], [70], [80], [90]])
y = np.array([500000, 600000, 700000, 800000, 900000])

modelo = LinearRegression()
modelo.fit(X, y)

prediccion = modelo.predict([[100]])

print("Precio estimado para una casa de 100 m²:", prediccion[0])