
import random
import numpy as np
import matplotlib.pyplot as plt



ITER = 100
E = 0.1
N = 10
greedy = 0
T = 0
tau = 5

Q = np.zeros([N, 4])
R = np.zeros([N, 1])
A = np.zeros([N, 1])
PLOT = np.zeros([ITER, 2])



def surround(t, a):
    for i in range(N):
        A[i, 0] = random.randint(-1000, 1000) / 1000
    R[:, 0] += (((t + 1) * (t + 1) - (t * t)) * A[:, 0]) / 2
    return R[a, 0]


def index():
    global Q
    max = -1000000
    pos = 0
    for i in range(N):
        if Q[i, 2] > max:
            max = Q[i, 2]
            pos = i
    return pos


def Quality(a, t):
    global Q, R, T
    T = 0
    M = 0
    for i in range(N):
        T += np.exp(Q[i, 2] / tau)
    # a -= 1
    Q[a, 0] += 1
    # Q[a, 1] += R[a, 0]
    # Q[a, 2] = Q[a, 1] / Q[a, 0]
    Q[a, 2] = M
    Q[a, 2] = M + 1 / (t + 1) * (surround(t, a) - M)
    if T != 0:
        Q[a, 3] = np.exp(Q[a, 2] / tau) / T
    PLOT[t, 0] = surround(t, a) / (t + 1)
    PLOT[t, 1] = Q[a, 2]


def Nchoice(c):
    S = random.choices(range(N), weights=Q[:, 3])
    while S[0] == c:
        S = random.choices(range(N), weights=Q[:, 3])
    return S[0]


for i in range(N):
    Quality(i, 0)
    # Q[i, 2] = random.random()
    # Q[i, 3] = random.random()
    T += np.exp(Q[i, 2] / tau)


greedy = index()


for i in range(ITER):
    way = random.random()
    if way <= E:
            act = Nchoice(greedy)
            Quality(act, i)
    else:
            Quality(greedy, i)
    greedy = index()
    plt.scatter(i, PLOT[i, 0], edgecolors='000')
    plt.scatter(i, PLOT[i, 1])
print(Q[:, 2], Q[:, 0], greedy, Q[greedy, 2])
plt.show()