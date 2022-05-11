import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
from scipy.optimize import fsolve


def plotIntersection(x, fx, gx):

    y1 = [fx(val) for val in x]
    y2 = [gx(val) for val in x]

    result = findIntersection(fx, gx)
    print(result)

    plt.plot(x, y1, x, y2, result, fx(result), "ro")

    plt.show()

    return 0


def findIntersection(fun1, fun2):
    temp = fsolve(lambda x: fun1(x) - fun2(x), (-10, 10))
    print(temp)
    return temp


f = lambda x: x ** 3 - x ** 2 + x
g = lambda x: 10 * x - 100
plotIntersection(np.linspace(-10, 10, 1000), f, g)

f = lambda x: x ** 2
g = lambda x: x + 10
plotIntersection(np.linspace(-10, 10, 1000), f, g)

f = lambda x: x*0 + 10
g = lambda x: x + 10
plotIntersection(np.linspace(-10, 10, 1000), f, g)

f = lambda x: x*0 + 10
g = lambda x: x*0 + 10
plotIntersection(np.linspace(-10, 10, 1000), f, g)

f = lambda x: x*0
g = lambda x: x*0 + 10
plotIntersection(np.linspace(-10, 10, 1000), f, g)
