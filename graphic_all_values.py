import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 3*x**2*y

def y_taylor(x, y, h):
    k1 = h * f(x, y)
    k2 = h**2 / 2 * (f(x, y) + x * f(x, y)**2)
    k3 = h**3 / 6 * (f(x, y) + 3 * x * f(x, y)**2 + x**2 * f(x, y)**3)
    k4 = h**4 / 24 * (f(x, y) + 4 * x * f(x, y)**2 + 6 * x**2 * f(x, y)**3 + x**3 * f(x, y)**4)
    return y + k1 + k2 + k3 + k4

x_min, x_max = 1, 1.5
h = 0.1
x = np.arange(x_min, x_max + h, h)

y_euler = np.zeros(len(x))
y_euler[0] = 1
for i in range(len(x) - 1):
    y_euler[i+1] = y_euler[i] + h*f(x[i], y_euler[i])

y_rk4 = np.zeros(len(x))
y_rk4[0] = 1
for i in range(len(x) - 1):
    k1 = f(x[i], y_rk4[i])
    k2 = f(x[i] + h/2, y_rk4[i] + (h/2)*k1)
    k3 = f(x[i] + h/2, y_rk4[i] + (h/2)*k2)
    k4 = f(x[i] + h, y_rk4[i] + h*k3)
    y_rk4[i+1] = y_rk4[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

y_taylor_4 = np.zeros(len(x))
y_taylor_4[0] = 1
for i in range(len(x) - 1):
    y_taylor_4[i+1] = y_taylor(x[i], y_taylor_4[i], h)

y_exact = np.exp(0.5*(x**3 - 1))
error_euler = np.abs(y_exact - y_euler)
error_rk4 = np.abs(y_exact - y_rk4)
error_taylor_4 = np.abs(y_exact - y_taylor_4)

print(" x    | y_exact | y_euler | y_rk4   | y_taylor_4 | error_euler | error_rk4   | error_taylor_4")
print("------|---------|---------|---------|------------|-------------|-------------|----------------")
for i in range(len(x)):
    print("{:.1f}  | {:.4f}  | {:.4f}  | {:.4f}  | {:.4f}     | {:.4f}      | {:.4f}      | {:.4f}".format(
        x[i], y_exact[i], y_euler[i], y_rk4[i], y_taylor_4[i], error_euler[i], error_rk4[i], error_taylor_4[i]))

plt.plot(x, y_exact, label='Solutia exacta', linestyle='--')
plt.plot(x, y_euler, label='Metoda Euler', linestyle='-.')
plt.plot(x, y_rk4, label='Metoda Runge-Kutta de ordin 4', linestyle=':')
plt.plot(x, error_euler, label='Metoda Euler eroare', linestyle='-.')
plt.plot(x, error_rk4, label='Metoda Runge-Kutta de ordin 4 eroare', linestyle=':')
plt.plot(x, y_taylor_4, label='Metoda Taylor de ordin 4', linestyle='-.')
plt.plot(x, error_taylor_4, label='Metoda Taylor de ordin 4 eroare', linestyle=':')


plt.legend() 
plt.show() 




