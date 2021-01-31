import numpy as np
import matplotlib.pyplot as plt

X, Y = np.meshgrid(np.arange(-8,6,1), np.arange(-6,7,1))
u, v = np.cos(X), np.sin(Y)
color_array = np.sqrt(v**2 + u**2)

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,u,v, color_array, width = 0.007)
ax.set_title('Carpet-like quiver plot')
ax.axis([-9, 6, -7, 7])
ax.set_aspect('equal')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_facecolor('ivory')

plt.show()