import numpy as np

class Simplex:
    def __init__(self, c, A, b):
        self.c = np.array(c, dtype=float)
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        
        # Add slack variables
        self.A = np.hstack((self.A, np.eye(len(self.b))))
        self.c = np.concatenate((self.c, np.zeros(len(self.b))))
        
        self.m, self.n = self.A.shape
        
    def solve(self):
        while True:
            # Find the pivot column
            j = np.argmax(self.c[:-len(self.b)])
            if self.c[j] <= 0:
                break
            
            # Find the pivot row
            ratios = self.b / self.A[:, j]
            ratios[ratios < 0] = np.inf
            i = np.argmin(ratios)
            
            # Do the pivot
            self.pivot(i, j)
        
        # Extract the solution and objective value
        x = np.zeros(self.n - len(self.b))
        for i in range(self.m):
            if np.sum(self.A[i, :-len(self.b)]) == 1 and np.sum(self.A[i, -len(self.b):]) == 1:
                x[np.argmax(self.A[i, :-len(self.b)])] = self.b[i]
        obj = -self.c[-1]
        
        return x, obj
        
    def pivot(self, i, j):
        # Scale pivot row
        self.A[i, :] /= self.A[i, j]
        self.b[i] /= self.A[i, j]
        
        # Update other rows
        for k in range(self.m):
            if k != i:
                self.A[k, :] -= self.A[k, j] * self.A[i, :]
                self.b[k] -= self.A[k, j] * self.b[i]
                
        # Update objective function
        self.c -= self.c[j] * self.A[i, :]
