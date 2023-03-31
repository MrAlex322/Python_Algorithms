import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = 2 * x + 3

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(x, y)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Linear Function')

plt.show()
