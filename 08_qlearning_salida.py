import numpy as np
import random

# Estados: 0, 1, 2, 3, 4
# Meta: estado 4
q_table = np.zeros((5, 2))  # acciones: 0 = izquierda, 1 = derecha

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for episodio in range(100):
    estado = 0

    while estado != 4:
        if random.uniform(0, 1) < epsilon:
            accion = random.randint(0, 1)
        else:
            accion = np.argmax(q_table[estado])

        if accion == 0:
            nuevo_estado = max(0, estado - 1)
        else:
            nuevo_estado = min(4, estado + 1)

        recompensa = 1 if nuevo_estado == 4 else 0

        q_table[estado, accion] = q_table[estado, accion] + alpha * (
            recompensa + gamma * np.max(q_table[nuevo_estado]) - q_table[estado, accion]
        )

        estado = nuevo_estado

print("Tabla Q aprendida:")
print(q_table)