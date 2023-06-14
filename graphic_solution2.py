import numpy as np
import matplotlib.pyplot as plt
def P(t):
 return (3000 / (1 - 0.4 * np.exp(-0.3 * t)))
t_values = np.linspace(0, 50, 500)
plt.plot(t_values, P(t_values))
plt.xlabel('t')
plt.ylabel('P(t)')
plt.title('Graficul solutiei P(t)')
plt.show()
