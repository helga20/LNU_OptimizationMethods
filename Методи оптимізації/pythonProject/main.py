import sympy as sym

x = sym.symbols('x')


def f(x):
    return round(x ** 2 + 3 * x + 3, 3)


def df(x):
    return round(2 * x + 3, 3)


max_iteration = 5


def newton_method(x0, eps):
    xi = x0
    i = 1
    checking = False
    while not checking and i <= max_iteration:
        print("Ітерація: ", i)
        func = f(xi)
        print("f(xi) = ", func)
        difunc = df(xi)
        print("f'(xi) = ", difunc)
        xi = round(xi - func / difunc, 3)
        print("xi = ", xi)
        if abs(func) < eps:
            checking = True
            break
        i += 1
    if checking:
        return "\n\nThe result was found! min =", xi
    else:
        return "\n\nThe result was not found with this number of iterations"


x0 = 3
h0 = 2

eps = 0.01
print(newton_method(x0, eps))