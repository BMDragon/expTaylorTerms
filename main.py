import numpy as np
import math
import matplotlib.pyplot as plt

# e^x = sum (x^n)/(n!) = 1 + x + x^2/2 + x^3/6 + ...

thresholds = np.array([0.1, 0.05, 0.01, 0.005, 0.001])

def expError(xVal, approx):
    truth = math.exp(xVal)
    return abs(truth - approx) / truth

def doCalc(xArr, thresh):
    ret = np.array([])
    for xx in xArr:
        i = 1; approx = 1
        while expError(xx, approx) > thresh:
            approx += (xx**i) / math.factorial(i)
            i += 1
        ret = np.append(ret, i)
    return ret

x = np.linspace(-10, 100, 1101)
plt.figure()
for th in thresholds:
    plt.plot(x, doCalc(x, th), label=th)
plt.legend()
plt.show()

