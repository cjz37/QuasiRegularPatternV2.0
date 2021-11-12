import math
import random
import numpy as np
from numba import jit


# 通过迭代生成h mtd=0
@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, mag=10, tp=0):
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

    if 0 == tp:
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


# 对h变换后直接得到k mtd=1
@jit(nopython=True)
def get_k_set(q, s, w, xmin, ymin, tp=0):
    pi = 3.1415927
    Q = q + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    k_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    if 0 == tp:
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + 5 * np.cos(x * coslist[i] + y * sinlist[i])
                k = abs(h)
                k = np.divmod(k, 16)[1]
                k_set[ny][nx] = k
    elif 1 == tp:
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
                if h < 0:
                    h1 = np.abs(h)
                elif h >= 0:
                    h1 = h + h1
                k = np.divmod(h1, 16)[1]
                k_set[ny][nx] = k

    return k_set


# 直接生成color_set mtd=2
@jit(nopython=True)
def get_color_set(q, s, w, xmin, ymin, tp=0):
    Q = q + 1
    W = w + 1
    xmax = xmin + s * np.pi
    ymax = ymin + s * np.pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    color_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)
    for i in range(1, Q):
        coslist[i] = np.cos(2 * np.pi * i / q)
        sinlist[i] = np.sin(2 * np.pi * i / q)
    kn = 0.05
    pw2kn = np.power(2, kn)

    Se1 = int(random.random() * 255 + 1)
    Se2 = int(random.random() * 255 + 1)
    Se3 = int(random.random() * 255 + 1)
    # 为保证图形一致先采用固定值
    Se1 = 239
    Se2 = 152
    Se3 = 16
    # Se1 = 253
    # Se2 = 24
    # Se3 = 11

    if 0 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
                t = np.log(np.abs(100 * h + 1e-6)) * pw2kn
                R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * t), 512)[1] - 256))
                G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * t), 512)[1] - 256))
                B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * t), 512)[1] - 256))
                if R > 255:
                    R = 255
                if G > 255:
                    G = 255
                if B > 255:
                    B = 255

                color_set[ny][nx] = B * 1e6 + G * 1e3 + R
    elif 1 == tp:
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + (np.cos(x * coslist[i] + y * sinlist[i]))
                Sinh = np.sin(h)
                Cosh = np.cos(h)
                R = 256 - int(np.abs(np.divmod(np.abs(Se1 - (1 * Se2 - 256) * np.exp(2 * Sinh + 1e-6) * kn), 512)[1]
                                     - 256))
                G = 256 - int(np.abs(np.divmod(np.abs(Se2 - (2 * Se3 - 256) * np.exp(3 * Cosh + 1e-6) * kn), 512)[1]
                                     - 256))
                B = 256 - int(np.abs(np.divmod(np.abs(Se3 - (3 * Se1 - 256) * np.exp(4 * Sinh + 1e-6) * kn), 512)[1]
                                     - 256))
                if R > 255:
                    R = 255
                if G > 255:
                    G = 255
                if B > 255:
                    B = 255

                color_set[ny][nx] = B * 1e6 + G * 1e3 + R

    return color_set
