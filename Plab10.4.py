import numpy as np
import matplotlib.pyplot as plt
def ctg(x):
    return 1 / np.tan(x)

plt.subplot(2, 2, 4)
plt.plot(x, ctg(x))
plt.show()