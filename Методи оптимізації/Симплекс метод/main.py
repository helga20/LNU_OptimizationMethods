import numpy as np


def Deltas(A, c, basis):
    deltas = np.array([], dtype='int')
    for i in range(len(A[1])):
        delta = c[basis[0]] * A[0][i] + c[basis[1]] * A[1][i] - c[i]
        deltas = np.append(deltas, delta)
    return deltas


def FindBasis(A):
    basis = np.array([], dtype='int')
    for j in range(len(A[1])):
        if A[0][j] == 0 and A[1][j] == 1:
            basis = np.append(basis, j)
        if A[0][j] == 1 and A[1][j] == 0:
            basis = np.append(basis, j)
    return basis


def checkDeltas(deltas):
    for i in range(len(deltas)):
        if deltas[i] > 0:
            return False
    return True


def checkOptimal(A, deltas):
    for j in range(len(A[1])):
        if A[0][j] < 0 and A[1][j] < 0 and deltas[j] < 0:
            return False
    return True


iteration = 1

# A = np.array([[0, 1, 1, 1, 1], [1, -1, 0, 1, 2]], dtype='float')
# b = np.array([3, 2], dtype='float')
# c = np.array([1, 1, 1, 1, 1])
# basis = np.array([2, 0])

A = np.array([[1, -5, -7, 0], [0, -39/2, -14, 1]], dtype='float')
b = np.array([-13, -28],  dtype='float')
c = np.array([-1, 10, -1, 0])
basis = FindBasis(A)

n = len(A)
print("Basis: ", basis)

while iteration <= n:
    print("A: \n ", A)
    deltas = Deltas(A, c, basis)
    print("Deltas: ", deltas)
    if not checkOptimal(A, deltas):
        print("функція не обмежена!! результату нема ")
        break
    if not checkDeltas(deltas):
        print("Result is not optimal")
        maxDelta = deltas[0]
        maxDeltaColumn = 0
        for i in range(len(deltas)):
            if deltas[i] > maxDelta:
                maxDelta = deltas[i]
                maxDeltaColumn = i

        print("max delta is: ", maxDelta)
        print("Main element column is :", maxDeltaColumn)

        Q = np.array([], dtype='int')
        for i in range(len(A)):
            Q = np.append(Q, b[i] / A[i][maxDeltaColumn])

        print(Q)

        minQ = Q[0]
        minQRow = 0
        for i in range(len(Q)):
            if minQ > Q[i] > 0:
                minQ = Q[i]
                minQRow = i

        print("Main element row is :", minQRow)
        mainElement = A[minQRow][maxDeltaColumn]
        print("Main element is: ", mainElement)

        print("Iteration", iteration)
        iteration += 1

        basis[minQRow] = maxDeltaColumn
        print("New basis")
        print(basis)

        for i in range(len(b)):
            if i != minQRow:
                b[i] = b[i] - ((b[minQRow] * A[i][maxDeltaColumn]) / A[minQRow][maxDeltaColumn])
            else:
                b[i] = b[i] / A[minQRow][maxDeltaColumn]

        print("New b: \n", b)
        for i in range(len(A)):
            for j in range(len(A[1])):
                if i != minQRow:
                    A[i][j] = A[i][j] - ((A[minQRow][j] * A[i][maxDeltaColumn]) / A[minQRow][maxDeltaColumn])

                else:
                    A[i][j] = A[i][j] / A[minQRow][maxDeltaColumn]

        print("New matrix: \n", A)

    else:
        print("Result is optiomal!")
        x = np.zeros(len(A[1]))
        for i in range(len(basis)):
            x[basis[i]] = b[i]
        print("Result:  ", x)

        function = 0
        for i in range(len(c)):
            function += c[i] * x[i]
        print("Function = ", function)
        break
