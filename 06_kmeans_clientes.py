from sklearn.cluster import KMeans
import numpy as np

datos = np.array([
    [60],
    [65],
    [70],
    [85],
    [90],
    [95]
])

modelo = KMeans(n_clusters=2, random_state=42, n_init=10)
modelo.fit(datos)

print("Grupos de alumnos:")
print(modelo.labels_)