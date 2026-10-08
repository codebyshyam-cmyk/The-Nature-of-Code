import matplotlib.pyplot as plt
import numpy as np


class Walker:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0

    def walk(self):
        choice = np.random.randint(0, 5)

        if choice == 1:
            self.x_position += 1
        elif choice == 2:
            self.x_position -= 1
        elif choice == 3:
            self.y_position += 1
        else:
            self.y_position -= 1


fig, ax = plt.subplots()

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

bear_grylls = Walker()

for i in range(1000):
    ax.scatter(bear_grylls.x_position, bear_grylls.y_position)
    bear_grylls.walk()

plt.show()