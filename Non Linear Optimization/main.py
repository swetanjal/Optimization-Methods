import numpy as np
import matplotlib.pyplot as plt
import json
import math
import scipy.optimize as optim

R = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,13,13,14,14,15,20,23,27,27,40,43,45,73,84,95,102,123,148,191,192,229,229,375,421,506,620,774,969,1080,1181,1359,1432,1768,2041,2463,2854,3273,3975,4370,5012,5498,5939]
I = [0,0,0,0,0,0,0,0,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,28,30,31,34,39,43,56,62,73,82,102,113,119,142,156,194,244,330,396,499,536,657,727,887,987,1024,1251,1397,1998,2543,2567,3082,3588,4778,5311,5916,6725,7598,8446,9205,10453,11487,12322,13430,14352,15722,17615,18539,20080,21370,23077,24530,26283]

R = np.array(R)
I = np.array(I)

S_0 = 15000
I_0 = 2
R_0 = 0
LAMBDA = 0.000001

beta = 0.00000089
gamma = 0.003
eta = 0.00001
for iterations in range(20):
    loss = 0
    Ipred = []
    Rpred = []
    Spred = []
    for i in range(len(R)):
        if i == 0:
            I_pred = I_0 + beta * I_0 * S_0 - gamma * I_0
            R_pred = R_0 + gamma * I_0
            S_pred = S_0 - beta * I_0 * S_0
            Ipred.append(I_pred)
            Rpred.append(R_pred)
            Spred.append(S_pred)
            loss = loss + (I[i] - I_pred) * (I[i] - I_pred) * LAMBDA + (1 - LAMBDA) * (R[i] - R_pred) * (R[i] - R_pred)
        else:
            I_pred = Ipred[i - 1] + beta * Ipred[i - 1] * Spred[i - 1] - gamma * Ipred[i - 1]
            R_pred = Rpred[i - 1] + gamma * Ipred[i - 1]
            S_pred = Spred[i - 1] - beta * Ipred[i - 1] * Spred[i - 1]
            Ipred.append(I_pred)
            Rpred.append(R_pred)
            Spred.append(S_pred)
            loss = loss + (I[i] - I_pred) * (I[i] - I_pred) * LAMBDA + (1 - LAMBDA) * (R[i] - R_pred) * (R[i] - R_pred)
    print(loss)
    db = 0
    dgamma = 0
    for i in range(len(R)):
        if i > 0:
            db = db + 2 * LAMBDA * (Ipred[i] - I[i]) * Ipred[i - 1] * Spred[i - 1]
            dgamma = dgamma + (-2 * LAMBDA) * (Ipred[i] - I[i]) * Ipred[i - 1] + (2 - 2 * LAMBDA) * (Rpred[i] - R[i]) * Ipred[i - 1]
        else:
            db = db + 2 * LAMBDA * (Ipred[i] - I[i]) * I_0 * S_0
            dgamma = dgamma + (-2 * LAMBDA) * (Ipred[i] - I[i]) * I_0 + (2 - 2 * LAMBDA) * (Rpred[i] - R[i]) * I_0
    beta = beta - eta * db
    gamma = gamma - eta * dgamma
    # print(beta)
    # print(gamma)
# print(R.shape)
# print(I.shape)
# def logistic(t, a, b, c):
#     return c / (1 + a * np.exp(-b * t))

# f = open('ind.json')
# data = json.load(f)['timelineitems'][0]
# x = []
# y = []
# time = 1
# for key in data.keys():
#     if key == 'stat':
#         continue
#     y.append((int(data[key]['total_cases'])))
#     x.append(time)
#     time = time + 1

# p0 = np.random.exponential(size = 3)
# bounds = (0, [100000., 3., 1000000000.])
# (a, b, c), cov =  optim.curve_fit(logistic, x, y, bounds=bounds, p0 = p0)
# print(a)
# print(b)
# print(c)


# # b = 0.138
# # a = 100
# # c = 40

# # for iteration in range(1000):
# #     L = 0
# #     for i in range(len(y)):
# #         L = L + (y[i] - c * 1.0 / (1 + a * math.exp(-b * i))) * (y[i] - c * 1.0 / (1 + a * math.exp(-b * i)))
# #     print(L)
# #     dc = 0
# #     for i in range(len(y)):
# #         dc = dc - 2 * (y[i] - c * 1.0 / (1 + a * math.exp(-b * i))) / (1 + a * math.exp(-b * i))
# #     da = 0
# #     for i in range(len(y)):
# #         da = da + 2 * (y[i] - c * 1.0 / (1 + a * math.exp(-b * i))) * c * math.exp(-b * i) / ((1 + a * math.exp(-b*i)) ** 2)
# #     db = 0
# #     for i in range(len(y)):
# #        db = db - 2 * (y[i] - c * 1.0 / (1 + a * np.exp(-b * i))) * (c * a / (1 + a * math.exp(-b*i))) * i * math.exp(-b * i) / ((1 + a * math.exp(-b*i)))
# #     a = a - 0.1 * da
# #     b = b - 0.001 * db
# #     c = c - 0.01 * dc
# #     # print(a)
# #     # print(b)
# #     # print(c)

# # print("*****************")
# # print(a)
# # print(b)
# # print(c)

# ls = []
# for i in range(200):
#     ls.append(c * 1.0 / (1 + a * np.exp(-b * i)))
# plt.plot(ls)
# plt.plot(y)
# plt.show()