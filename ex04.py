
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 150)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(2*x))
plt.show()
