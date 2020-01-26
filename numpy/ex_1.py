import numpy as np
def mul_tabel():
    a = np.arange(0, 11)
    b = np.arange(0, 11).reshape(11,1)
    c = a*b
    # d = c + b
    # d = c + a
    # # c[1:11,0:1] = 1
    return c

def fancy():
    a = np.arange(25).reshape(5, 5)
    a[0:5, 1:4] = 0
    a[0:5, 4:5] = 1
    a[0:5, 0:1] = 1
    return a




if __name__ == '__main__':
    print(mul_tabel())
    print(fancy())
