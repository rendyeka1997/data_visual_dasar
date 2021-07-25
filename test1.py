import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([8, 9, 10, 11, 12])

plt.hist(a, bins=20)
plt.hist(b, bins=20)
plt.show()
