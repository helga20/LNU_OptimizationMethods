import numpy as np
from scipy.optimize import linprog


def get_duality(A, b, c):
    return A.T, c, b


def print_problem(A, b, c):
    print('A:\n', A)
    print('b:\n', b)
    print('c:\n', c)


if __name__ == '__main__':
    c = np.array(
        [1, 2])

    A = np.array([
        [5, -2],
        [-1, 2],
        [1, 1],
    ])

    b = np.array(
        [4, 4, 4])

    bounds = [(0, None)] * len(c)

    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    print('result:\n', result)

    # get duality problem
    A_d, b_d, c_d = get_duality(A, b, c)
    d_bounds = [(0, None)] * len(c_d)

    d_result = linprog(c_d, A_ub=A_d, b_ub=b_d,
                       bounds=d_bounds, method='highs')
    print('duality_result:\n', d_result)
