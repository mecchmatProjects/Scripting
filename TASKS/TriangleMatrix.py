import random
import numpy

matrix = [[1,2,3],[1,2,3]]

matrix = []
n = 3
points = []
for i in range(n):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    points.append([i, x, y])



for i in range(len(points)):
    for j in range(i+1, len(points)):
            matrix.append([
                points[i],
                points[j]
            ])

len(matrix)
len(matrix[0])



def get_higher_tr(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    
    for i in range( 0, len(matrix) ):
        for j in range( 0, len(matrix[0]) ):
            if i <= j and matrix[i][j] == 0: return False
            if i > j and matrix[i][j] != 0: return False
    
    return True

    
def get_lower_tr(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    
    for i in range( 0, len(matrix) ):
        for j in range( 0, len(matrix[0]) ):
            if i >= j and matrix[i][j] == 0: return False
            if i < j and matrix[i][j] != 0: return False
    
    return True

matrix = numpy.array(matrix)
get_h_vectorized = numpy.vectorize(get_higher_tr, signature='(m,n)->()')
get_l_vectorized = numpy.vectorize(get_lower_tr, signature='(m,n)->()')

#Proofs
matrix1 = [[1,2,3],[0,2,3],[0,0,3]]
matrix2 = [[1,0,0],[1,2,0],[1,2,3]]
matrix3 = [[0,0,0],[0,0,0],[0,0,0]]
matrix1 = numpy.array(matrix1)
matrix2 = numpy.array(matrix2)
matrix3 = numpy.array(matrix3)

get_h_vectorized(matrix1)
get_h_vectorized(matrix2)

get_l_vectorized(matrix1)
get_l_vectorized(matrix2)

get_l_vectorized(matrix3)
get_h_vectorized(matrix3)



