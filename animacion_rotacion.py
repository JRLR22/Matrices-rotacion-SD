import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================
# Funciones de rotación
# =========================
def rot_x(x, y, z, theta):
    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    return R @ p

def rot_y(x, y, z, theta):
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ p

def rot_z(x, y, z, theta):
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ p

# =========================
# Animación
# =========================
punto = np.array([1, 0, 0])  # punto inicial

theta_x = np.radians(0)
theta_y = np.radians(0)
theta_z = np.radians(90)  # giro de 90° en Z

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Punto y trazo
scat = ax.scatter(*punto, color="red", s=50, label="Punto en movimiento")
linea, = ax.plot([], [], [], color="blue", lw=2, label="Trayectoria")

# Texto a la derecha
texto = ax.text2D(1.05, 0.8, "", transform=ax.transAxes)

# Límites
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.legend()

trayectoria = []

def actualizar(frame):
    frac = frame / 100
    p_rot = rot_x(*punto, theta_x * frac)
    p_rot = rot_y(*p_rot, theta_y * frac)
    p_rot = rot_z(*p_rot, theta_z * frac)

    # Actualizar punto
    scat._offsets3d = ([p_rot[0]], [p_rot[1]], [p_rot[2]])

    # Guardar trayectoria
    trayectoria.append(p_rot)
    trayectoria_arr = np.array(trayectoria)
    linea.set_data(trayectoria_arr[:, 0], trayectoria_arr[:, 1])
    linea.set_3d_properties(trayectoria_arr[:, 2])

    # Mostrar texto con coordenadas
    texto.set_text(
        f"Original: {punto}\n"
        f"Rotado: [{p_rot[0]:.2f}, {p_rot[1]:.2f}, {p_rot[2]:.2f}]"
    )

    return scat, linea, texto

ani = FuncAnimation(fig, actualizar, frames=201, interval=100, blit=False)

#Para que funcione el guardado de la animacion se ocupa tener pillow instalado con este comando "pip install pillow"

# Guardar la animación como GIF
ani.save("rotacion.gif", writer="pillow", fps=10)

# Mostrar en pantalla (opcional)
plt.show()
