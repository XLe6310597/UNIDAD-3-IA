import numpy as np
import random

q_table = np.zeros((7, 2))  # 7 estados, 2 acciones

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for episodio in range(200):
    estado = 0

    while estado != 6:
        if random.uniform(0, 1) < epsilon:
            accion = random.randint(0, 1)
        else:
            accion = np.argmax(q_table[estado])

        if accion == 0:
            nuevo_estado = max(0, estado - 1)
        else:
            nuevo_estado = min(6, estado + 1)

        recompensa = 10 if nuevo_estado == 6 else -1

        q_table[estado, accion] = q_table[estado, accion] + alpha * (
            recompensa + gamma * np.max(q_table[nuevo_estado]) - q_table[estado, accion]
        )

        estado = nuevo_estado

print("Tabla Q aprendida:")
print(q_table)