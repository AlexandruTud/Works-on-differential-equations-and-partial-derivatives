import numpy as np
import matplotlib.pyplot as plt
K = 3000
r = 0.3
N0 = 1000
def N(t):
 return K / (1 + (K-N0)/N0*np.exp(-r*t))
t = np.linspace(0, 20,100)
plt.plot(t, N(t))
plt.xlabel('Timpul (ani)')
plt.ylabel('Numarul de cai')
plt.show()