from sympy import *
x = Symbol('x')

a = -3
b = 3
L = 9
f = x ** 2 + 3 * x + 3
x_i = -3
e = 0.01

q_list = []
ro_max = []


q_list.append(f.evalf(subs={x: x_i}) - L * abs(x - x_i))
iteration_check = true


def check(check_ro, xi, e):
    if abs(check_ro - f.evalf(subs={x: xi})) < e:
        print("\nПеревірка:")
        print("|", check_ro, "-", int(f.evalf(subs={x: xi})), "| < ", e)
        return True
    print("Перевірка:")
    print("|", check_ro, "-", int(f.evalf(subs={x: xi})), "| > ", e, "Продовжуємо ітерації..")
    return False


for i in range(5):
    print("\n\nIteration ", i)
    ro = []
    q = []
    p_min_index = 100
    ro_to_check = 0
    if i == 0:
        for k in range(a, b + 1):
            ro.append(int(q_list[-1].evalf(subs={x: k})))
            if ro[-1] < p_min_index:
                p_min_index = k
                ro_to_check = ro[-1]
        x_i = p_min_index
    else:
        l = a
        for k in range(len(ro_max)):
            ro.append(int(ro_max[k]))
            if ro[-1] < p_min_index:
                x_i = l
                p_min_index = ro[-1]
                ro_to_check = ro[-1]
            l += 1

    print("Xi =", x_i)
    print("P:", ro)
    q_list.append(f.evalf(subs={x: x_i}) - L * abs(x - x_i))
    for k in range(a, b + 1):
        q.append(int(q_list[-1].evalf(subs={x: k})))
    print("q:", q)

    ro_max = []
    for k in range(len(ro)):
        ro_max.append(int(max(ro[k], q[k])))

    print("P_max:", ro_max)

    if check(ro_to_check, x_i, e):
        print("\nПеревірку пройдено!")
        result = f.evalf(subs={x: x_i})
        print("\nf min = ", int(result))
        iteration_check = false
        break


if iteration_check:
    print("Досягнуто максимальної кількості ітерацій")








