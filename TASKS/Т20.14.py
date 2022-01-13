import random
import numpy

points = []
n = 100

for i in range(n):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    points.append([i, x, y])

triangles = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        for k in range(j+1, len(points)):
            triangles.append([
                points[i],
                points[j],
                points[k]
            ])

triangles = numpy.array(triangles)

def get_s(triangle):
    _, x1, y1 = triangle[0]
    _, x2, y2 = triangle[1]
    _, x3, y3 = triangle[2]
    return abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))/2

get_s_vectorized = numpy.vectorize(get_s, signature='(m,n)->()')

s = get_s_vectorized(triangles)

max_s_value = max(s)
max_s_index = numpy.where(s == max_s_value)[0][0]
print('Max S: ', max_s_value)
print('Points: ')
for i, x, y in triangles[max_s_index]:
    print('Index:', i, f', values: ({x},{y})')