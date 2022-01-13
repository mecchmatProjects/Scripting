import numpy

hat = numpy.concatenate((
    [0 for red in range(4)],
    [1 for blue in range(4)],
    [2 for black in range(4)]
))

def simulate(step):
    choose =  numpy.random.choice(hat, 3, replace=False)
    return numpy.count_nonzero(choose == 2) >= 2

simulate_v = numpy.vectorize(simulate)

size = 100000
rez = numpy.zeros(size)
rez = simulate_v(rez)
rez = numpy.count_nonzero(rez) / size

print(f'Probability is about {round(rez*100, 1)}%')