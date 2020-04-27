import numpy as np
Ix = []
Iy = []
for i in range(100):
    Ix.append(i)
    Iy.append(i - 1)

X = np.stack((Ix, Iy), axis=0)
C = np.cov(X)
print(C)
w, v = np.linalg.eig(C)
print(w)
print(v)