import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rotacion  # importa las funciones de rotacion.py

# Nota para que no se me olvide: con Python3 instalar con el comando: "pip install numpy matplotlib" 
# para ver la grafica 3D (ya que matplotlib es para la creacion del grafico y ver datos)

# Punto original
p = np.array([1, 2, 3])

# Rotación alrededor del eje Z, 90 grados
theta = np.radians(290)
p_rot = rotacion.rotar(*p, theta, axis="z")

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(*p, color="red", label="Original")
ax.scatter(*p_rot, color="blue", label="Rotado")

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.legend()
plt.show()
