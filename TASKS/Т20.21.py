import random
import numpy

K = 1000
N = 2000
STEP = 100

def simulate(i,P):
    k = K
    while True:
        if k - STEP < 0:
            return 0
        elif k >= N:
            return 1
        if random.random() <= P:
            k += STEP
        else:
            k -= STEP

simulate_vectorized = numpy.vectorize(simulate)

for i in range(10):
    result = simulate_vectorized(numpy.zeros(1000), (i+1)/10)
    print('P:', (i+1)/10, 'rez:',sum(result)/len(result)) 