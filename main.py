
import random
import numpy as np
import math

E = 0.1
N = 10
Q = np.zeros([N, 4])
R = np.zeros([N, 1])
A = np.zeros([N, 1])
greedy = 0
T = 0
tau = 5

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
    for i in range(N):
        T += np.exp(Q[i, 2] / tau)
    a -= 1
    Q[a, 0] += 1
    Q[a, 1] += R[a, 0]
    Q[a, 2] = Q[a, 1] / Q[a, 0] + (1 / (t + 1) * ((((t + 2) * (t + 2) - (t + 1) * (t + 1)) * A[a, 0]) / 2 - Q[a, 1] / Q[a, 0]))
    Q[a, 3] = np.exp(Q[a, 2] / tau) / T

def Nchoice(c):
    S = random.choices(range(N), weights=Q[:, 3])
    while S[0] == c:
        S = random.choices(range(N), weights=Q[:, 3])
    return S[0]


# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self, color, doors, tires, vtype):
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
#         self.vtype = vtype
#
#     def brake(self):
#         """
#         Stop the car
#         """
#         return "%s braking" % self.vtype
#
#     def drive(self):
#         """
#         Drive the car
#         """
#         return "I'm driving a %s %s!" % (self.color, self.vtype)
#
#
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4, "car")
#     print(car.brake())
#     print(car.drive())
#
#     truck = Vehicle("red", 3, 6, "truck")
#     print(truck.drive())
#     print(truck.brake())

for i in range(N):
    Q[i, 2] = random.random()
    Q[i, 3] = random.random()
    A[i, 0] = random.randint(-1000, 1000) / 100000
    T += np.exp(Q[i, 2] / tau)

greedy = index()

for i in range(100):
    R[:, 0] += (((i + 1) * (i + 1) - (i * i)) * A[:, 0]) / 2
    way = random.random()
    if i < 100:
        if way <= E:
            act = Nchoice(greedy)
            Quality(act, i)
        else:
            Quality(greedy + 1, i)
    else:
        Quality(greedy + 1, i)
    greedy = index()
print(Q[:, 2], Q[:, 0], greedy, Q[greedy, 2])