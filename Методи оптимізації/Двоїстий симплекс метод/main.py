import numpy as np
from scipy.optimize import linprog


def print_dual(matrix_a, vector_b, vector_c):
    dual_a = []
    dual_c = vector_b
    dual_b = vector_c
    print("Двоїста матриця A:")
    for i in range(len(matrix_a[1])):
        row = []
        for j in range(len(matrix_a)):
            row.append(matrix_a[j][i])
        print(row)
        dual_a.append(row)

    print("Двоїстий вектор b:")
    print(dual_b)
    print("Двоїстий вектор c:")
    print(dual_c)


c = [1, 1, 2]
A = [[3, 4, -1], [1, -1, 2], [2, 0, 1]]
b = [4, 6, 5]
bounds = [(0, None), (0, None), (0, None)]

print_dual(A, b, c)
#
#
# c = [4, 6, 5, 0, 0, 0]
# A_eq = [[3, 1, 2, -1, 0, 0], [4, -1, 0, 0, -1, 0], [-1, 2, 1, 0, 0, -1]]
# b_eq = [1, 1, 2]
# bounds = [(0, None), (0, None),  (0, None), (0, None), (0, None), (0, None)]

res = linprog(c=c, A_eq=A, b_eq=b, bounds=bounds, method='highs')

if res.success:
    print("x =", res.x)
    print("f(x) =", res.fun)
else:
    print("Функція необмежена")
