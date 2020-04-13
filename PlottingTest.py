import matplotlib.pyplot as plt
import numpy as np
import math

def gaussian(x, alpha, r):
    return 1./(math.sqrt(alpha**math.pi))*np.exp(-alpha*np.power((x - r), 2.))


x = np.linspace(-3, 3, 100)
plt.plot(x, gaussian(x, 1, 0))

plt.show()
