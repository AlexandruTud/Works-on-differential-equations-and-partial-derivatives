import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
 return 3*x**2*y
x_min, x_max = 1, 1.5
h = 0.1
x = np.arange(x_min, x_max + h, h)
y_euler = np.zeros(len(x))
y_euler[0] = 1
for i in range(len(x) - 1):
 y_euler[i+1] = y_euler[i] + h*f(x[i], y_euler[i])
y_exact = np.exp(0.5*(x**3 - 1))
error_euler = np.abs(y_exact - y_euler)
print(" x | y_exact | y_euler | error ")
print("------|---------|---------|--------")
for i in range(len(x)):
 print(" {:.1f} | {:.4f} | {:.4f} | {:.4f}".format(x[i], y_exact[i], y_euler[i], 
error_euler[i]))
# Plot the solutions
plt.plot(x, y_exact, label='Exact solution')
plt.plot(x, y_euler, label='Euler method')
plt.legend()
plt.show()
# Plot the error
plt.plot(x, error_euler, label='Euler method error')
plt.legend()
plt.show()
