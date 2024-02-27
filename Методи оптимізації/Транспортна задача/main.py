from pulp import *

d = [45, 15, 30]  # запаси
s = [20, 22, 18, 30]  # потреби
c = [[9, 7, 8, 4], [6, 6, 7, 5], [4, 7, 9, 5]]  # тариф

x = []
for i in range(len(d)):
    x.append([])
    for j in range(len(s)):
        x[i].append(LpVariable("x%d%d" % (i, j), lowBound=0))


problem = LpProblem("Transportation_Problem", LpMinimize)


cost = []
for i in range(len(d)):
    cost.append([])
    for j in range(len(s)):
        cost[i].append(c[i][j] * x[i][j])
problem += lpSum(item for list in cost for item in list)


for i in range(len(d)):
    problem += lpSum(x[i]) <= d[i]
for j in range(len(s)):
    problem += lpSum([x[i][j] for i in range(len(d))]) == s[j]
problem.solve()

print("Значення опорного плану")
for i in range(len(d)):
    for j in range(len(s)):
        print("[%d,%d] = %d" % (i+1, j+1, x[i][j].varValue))

print("Значення цільової функції =", value(problem.objective))