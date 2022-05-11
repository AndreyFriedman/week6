import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
from scipy.optimize import fsolve


def plotIntersection(param, fx, gx):
    x = param
    y1 = [fx(val) for val in x]
    y2 = [gx(val) for val in x]


    result1 = findIntersection(fx, gx)
    print(result1)

    plt.plot(x, y1, x, y2, result1, fx(result1), "ro")
    # plt.plot(result1, fx(result1), "ro")

    plt.show()

    return 0


def findIntersection(fun1, fun2):
    bap = fsolve(lambda x: fun1(x) - fun2(x), (-10, 10))
    print(bap)
    return bap


f = lambda x:  x**3 - x**2 + x
g = lambda x:  10*x - 100

plotIntersection(np.linspace(-10, 10, 1000), f, g)
