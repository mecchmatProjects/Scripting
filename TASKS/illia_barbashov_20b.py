import math

import numpy as np

def sign(a):
    """
    Аналог функції sign, але без нуля
    :param a: довільне число
    """
    return -1 if a < 0 else 1

def custom_cos(angle, n):
    """
    :param angle: кут для якого рахувати косинус
    :param n: кількість елементів в послідовності (точність)
    :return: косинус кута
    """
    arr = np.array([ (-1)**el[0]*el[1] for el in zip(range(0, n//2),range(0, n, 2)) ])

    cos_lam = lambda el: sign(el)*(angle**abs(el))/math.factorial(abs(el))
    vcos = np.vectorize(cos_lam)
    return np.sum(vcos(arr))

if __name__ == '__main__':
    print(custom_cos(math.pi/2, 15))
    print(custom_cos(math.pi/3, 15))
    print(custom_cos(math.pi/4, 15))
    print(custom_cos(math.pi/6, 15))
    print(custom_cos(math.pi, 15))
    print(custom_cos(0, 15))


