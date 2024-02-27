import matplotlib.pyplot as plt
import numpy as np

colors = ["red", "pink", "green", "blue", "purple", "#006400", "#000080"]

a = []
b = []
c = []
znak = []
size = int(input("How many inequalities do you have? "))
for i in range(size):
    print("Enter coefficients of inequality: ")
    a.append(float(input("a: ")))
    b.append(float(input("b: ")))
    c.append(float(input("c: ")))
    znak.append(input("Enter znak <= or >= : "))


fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


for i in range(size):
    x = np.arange(-5, 5, 1)
    y = (c[i] - a[i] * x) / b[i]
    ax.plot(x, y, color=colors[i])
    if znak[i] == ">=" or b[i] < 0:
        ax.fill_between(x, 6, y, color=colors[i], alpha=0.2)
    else:
        ax.fill_between(x, -6, y, color=colors[i], alpha=0.2)

plt.show()
