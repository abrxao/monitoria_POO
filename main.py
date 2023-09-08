
import matplotlib.pyplot as plt
from model import Hexagono

fig, ax = plt.subplots()

hexagono = Hexagono(2, (0,0))
hexagono.desenhar(ax)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()