import numpy

matrix = numpy.array([
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
])

cols_sum = numpy.sum(matrix, axis=0)
rows_sum = numpy.sum(matrix, axis=1)

rez = numpy.concatenate((cols_sum, rows_sum), axis=0)
rez = rez == rez[0]
rez = rez.all()

print('It`s magic square' if rez else 'It`s NOT magic square')