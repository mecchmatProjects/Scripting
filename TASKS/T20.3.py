import matplotlib.pyplot as plt
import math
import numpy

def f(x, m):
    y = 0
    for i in range(m):
        p = i*2+1
        y += x**p/math.factorial(p)
    return y

f_vectorized = numpy.vectorize(f)

m = 30
mm = list(range(1, m+1))

a = -100
b = 100
xx = list(range(a, b+1))

for m in mm:
    plt.clf()
    yy = f_vectorized(xx, m)
    plt.plot(xx, yy)
    plt.savefig(f'T20.3/{m}.png')