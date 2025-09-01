import numpy as np

# Definir matrices de rotación
def Rx(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def Ry(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def Rz(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# Definir un punto
punto = np.array([1, 2, 3])

# Definir ángulos en grados y convertir a radianes
theta_x = np.radians(30)
theta_y = np.radians(45)
theta_z = np.radians(60)

# Matriz de rotación compuesta
rotacion_total = Rx(theta_x) @ Ry(theta_y) @ Rz(theta_z)

# Aplicar rotación
punto_rotado = rotacion_total @ punto

print("Punto original:", punto)
print("Punto rotado:", punto_rotado)
