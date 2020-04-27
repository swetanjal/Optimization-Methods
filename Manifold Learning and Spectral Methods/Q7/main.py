import numpy as np
from sklearn.cluster import KMeans
f = open('main.txt', 'r')
f = f.readlines()

X = []
for line in f:
    tok = line.split(',')
    X.append(np.array([float(tok[0]), float(tok[1])]))
X = np.array(X)

avg1x = 0
avg1y = 0
avg2x = 0
avg2y = 0
for i in range(50):
    avg1x += X[i][0]
    avg1y += X[i][1]
for i in range(50, 100):
    avg2x += X[i][0]
    avg2y += X[i][1]
avg1x = avg1x / 50
avg1y = avg1y / 50
avg2x = avg2x / 50
avg2y = avg2y / 50
print(avg1x, " ",  avg1y)
s = 0
for i in range(50):
    s = s + (X[i][0] - avg1x) ** 2 + (X[i][1] - avg1y) ** 2
for i in range(50, 100):
    s = s + (X[i][0] - avg2x) ** 2 + (X[i][1] - avg2y) ** 2
print(s)
kmeans = KMeans(n_clusters=2, init=np.array([np.array([avg1x, avg1y]), np.array([avg2x, avg2y])]), max_iter=100, n_init=1).fit(X)
print(kmeans.inertia_)
print(kmeans.labels_)