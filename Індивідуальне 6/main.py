import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * x**2 - x + 2


def f_prime(x):
    return 4 * x - 1


def newton(x0, e, iterations=100):
    for i in range(iterations):
        fx0 = f(x0)
        fprimex0 = f_prime(x0)
        print(f"ITERATION {i}")
        print("x =", x0, "\nf(x) =", f(x0), "\nf'(x) =", f_prime(x0))

        # plot
        x = np.linspace(-1, 1, 100)
        y = f(x)
        plt.plot(x, y)

        # plot tangent
        y1 = fprimex0 * (x - x0) + fx0
        plt.plot(x, y1, "-r")

        x1 = x0 - fx0 / fprimex0
        if abs(x1 - x0) < e:
            return x1
        x0 = x1
    return x0


x0 = 1
e = 0.01
iterations = 5

result = newton(x0, e, iterations)

print("min:", result)

plt.grid()
plt.show()
