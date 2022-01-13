import numpy as np
import numpy.linalg as la


def ortho_check(Q):
    """
    Нехай Q задана матриця, якщо матриця ортонормована, то за спектральною теоремою Q*Q^T=I, використаємо дану властивість для перевірки.
    :param arr:
    :return:
    """
    sh = Q.shape
    if sh[0] != sh[1]:
        # not a square matrix
        return False
    I = np.eye(sh[0])
    QI =  Q.dot(Q.T)
    return np.allclose(QI, I, )

if __name__ == '__main__':
    arr = np.array([
        [2,7,11],
        [24,5,16],
        [17,13,11]
    ])
    q,r = la.qr(arr)
    print(q)
    print(ortho_check(q))