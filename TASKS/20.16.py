import numpy as np
a = int(input("Size of array: "))


A = [np.array([input().split()],int) for _ in range(a)]
B = np.array(A)
#найбільший елемент кожного рядка
C = (B.max(axis=1)).max(axis = 1)
#найменший серед найбільших елементів рядків
d = C.min()
print (d)




