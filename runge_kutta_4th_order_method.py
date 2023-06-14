import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
 return 3*x**2*y
x_min, x_max = 1, 1.5
h = 0.1
x = np.arange(x_min, x_max + h, h)
y_rk4 = np.zeros(len(x))
y_rk4[0] = 1
for i in range(len(x) - 1):
 k1 = f(x[i], y_rk4[i])
 k2 = f(x[i] + h/2, y_rk4[i] + (h/2)*k1)
 k3 = f(x[i] + h/2, y_rk4[i] + (h/2)*k2)
 k4 = f(x[i] + h, y_rk4[i] + h*k3)
 y_rk4[i+1] = y_rk4[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
y_exact = np.exp(0.5*(x**3 - 1))
error_rk4 = np.abs(y_exact - y_rk4)
print(" x | y_exact | y_rk4 | error ")
print("------|---------|---------|--------")
for i in range(len(x)):
 print("{:.1f} | {:.6f} | {:.6f} | {:.6f}".format(x[i], y_exact[i], y_rk4[i], 
error_rk4[i]))
plt.plot(x, y_exact, label='Solutia exacta')
plt.plot(x, y_rk4, label='Metoda Runge-Kutta de ordin 4')
plt.legend()
plt.show()
plt.plot(x, error_rk4, label='Metoda Runge-Kutta de ordin 4 eroare')
plt.legend()
plt.show()