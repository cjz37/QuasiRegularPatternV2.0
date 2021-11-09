import math
import numpy as np
from numba import jit


@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, mag, tp=0):
    pi = 3.1415927
    Q = q + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    for i in range(1, Q):
        coslist[i] = np.cos(2 * pi * i / q)
        sinlist[i] = np.sin(2 * pi * i / q)
    for nx in range(W):
        for ny in range(W):
            x = xmin + (nx - halfw) * deltax
            y = ymin + (ny - halfw) * deltay
            h = 0
            for i in range(1, Q):
                h = h + np.cos(x * coslist[i] + y * sinlist[i])
            h1 = math.ceil(h * mag)
            h_set[ny][nx] = h1

    return h_set
