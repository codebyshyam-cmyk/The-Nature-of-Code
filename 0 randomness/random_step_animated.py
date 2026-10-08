import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class Walker:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0

    def walk(self):
        
        dx,dy = directions[np.random.randint(0,9)]
        self.x_position += dx
        self.y_position += dy

        # if choice == 0:
        #     self.x_position += 5
        # elif choice == 1:
        #     self.x_position -= 5
        # elif choice == 2:
        #     self.y_position += 5
        # else:
        #     self.y_position -= 5

directions = [
    (-4, -4),  # ↙
    (-4,  0),  # ←
    (-4,  4),  # ↖
    ( 0, -4),  # ↓
    ( 0,  0),  # stay
    ( 0,  4),  # ↑
    ( 4, -4),  # ↘  
    ( 4,  0),  # →
    ( 4,  4)   # ↗
]

walker = Walker()

fig, ax = plt.subplots()

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_aspect("equal")

x_history = []
y_history = []

# The point representing our walker
point, = ax.plot([], [], "o")
trail, = ax.plot([],[],"-")


def update(frame):
    walker.walk()
    x_history.append(walker.x_position)
    y_history.append(walker.y_position)

    point.set_data([walker.x_position], [walker.y_position])
    trail.set_data(x_history,y_history)

    return point,trail


animation = FuncAnimation(
    fig,
    update,
    frames=1000,
    interval=50,       # milliseconds between steps
    blit=True
)

plt.show()
