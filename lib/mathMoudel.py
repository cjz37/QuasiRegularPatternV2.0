import math
import random
import numpy as np
from numba import jit


# 通过迭代生成h mtd=0
@jit(nopython=True)
def get_h_set(q, s, w, xmin, ymin, mag=10, tp=0):
    pi = 3.1415927
    # Q = q + 1
    Q = round(q) + 1
    W = w + 1
    xmax = xmin + s * pi
    ymax = ymin + s * pi
    deltax = (xmax - xmin) / w
    deltay = (ymax - ymin) / w
    h_set = [[0 for col in range(W)] for row in range(W)]
    halfw = w / 2
    coslist = np.zeros(Q)
    sinlist = np.zeros(Q)

    if 0 == tp:  # 4 浮点型q
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
    elif 1 == tp:  # 4 参数i设计一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(i * x * coslist[i] + i * y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 2 == tp:  # 4 参数i设计二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + i * np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 3 == tp:  # 4 参数i设计三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i] + i)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 4 == tp:  # 4 参数i设计四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + i/8
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 5 == tp:  # 4 其他参数设计一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + 2 * np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 6 == tp:  # 4 其他参数设计二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q + 0.5)
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
    elif 7 == tp:  # 4 其他参数设计三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 8 == tp:  # 4 其他参数设计四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + 1
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 9 == tp:  # 4 其他参数设计五
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(3.5 * x * coslist[i] + 1.5 * y * sinlist[i] + 0.5) + 1
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 10 == tp:  # 5 绝对值变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * np.pi * i / q)
            sinlist[i] = np.sin(2 * np.pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 11 == tp:  # 5 局部绝对值变换
        for i in range(1, Q):
            coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
            sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 12 == tp:  # 5 复合绝对值变换
        for i in range(1, Q):
            coslist[i] = np.abs(np.cos(2 * np.pi * i / q))
            sinlist[i] = np.abs(np.sin(2 * np.pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 13 == tp:  # 5 结合参数绝对值
        for i in range(1, Q):
            coslist[i] = np.cos(2 * np.pi * i / q)
            sinlist[i] = np.sin(2 * np.pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(i * np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 14 == tp:  # 5 整体三角变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sin(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 15 == tp:  # 5 整体三角变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 16 == tp:  # 5 整体三角变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + 1 / np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 17 == tp:  # 5 整体三角变换四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 18 == tp:  # 5 整体三角变换五
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sin(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 19 == tp:  # 5 整体三角变换六
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 20 == tp:  # 5 整体三角变换七
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 21 == tp:  # 5 整体三角变换八
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.tan(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 22 == tp:  # 5 局部三角变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * sinlist[i] + y * coslist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 23 == tp:  # 5 局部三角变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x / coslist[i] + y / sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 24 == tp:  # 5 局部三角变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 25 == tp:  # 5 自变量三角变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                cosx = np.cos(x)
                siny = np.sin(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 26 == tp:  # 5 自变量三角变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                tanx = np.tan(x)
                if 0 == y:
                    y = 1
                rtany = 1 / np.tan(y)  # 除数可能为0，偏移量须设为非0
                # rtany = 1
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(tanx * coslist[i] + rtany * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 27 == tp:  # 5 整体与局部复合三角变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.abs(np.cos(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 28 == tp:  # 5 整体与局部复合三角变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(np.abs(np.sin(x * coslist[i]) + np.cos(y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 29 == tp:  # 5 整体与自变量复合三角变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.tan(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 30 == tp:  # 5 整体与自变量复合三角变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.abs(cosx * coslist[i] + siny * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 31 == tp:  # 5 局部与自变量复合三角变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                cosx = np.cos(x)
                siny = np.sin(y)
                for i in range(1, Q):
                    h = h + np.cos(np.tan(cosx * coslist[i]) + np.tan(siny * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 32 == tp:  # 5 整体幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 33 == tp:  # 5 整体幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 34 == tp:  # 5 整体幂函数变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 15)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 35 == tp:  # 5 整体幂函数变换四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 36 == tp:  # 5 整体幂函数变换五
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 2)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 37 == tp:  # 5 整体幂函数变换六
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 38 == tp:  # 5 整体幂函数变换七
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.sqrt(np.abs(np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 39 == tp:  # 5 局部幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 40 == tp:  # 5 局部幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 3)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 3)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 41 == tp:  # 5 局部幂函数变换三
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 15)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 15)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 42 == tp:  # 5 局部幂函数变换四
        for i in range(1, Q):
            coslist[i] = np.sqrt(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.sqrt(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 43 == tp:  # 5 自变量幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 44 == tp:  # 5 自变量幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.power(np.abs(x), 0.75)
                Y = np.power(np.abs(y), 0.75)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 45 == tp:  # 5 自变量幂函数变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.power(np.abs(x), 1.25)
                Y = np.power(np.abs(y), 1.25)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 46 == tp:  # 5 自变量幂函数变换四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sin(np.sqrt(np.abs(x)))
                Y = np.cos(np.sqrt(np.abs(y)))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 47 == tp:  # 5 整体与局部复合的幂函数变换
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(x * coslist[i] + y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 48 == tp:  # 5 整体与自变量复合的幂函数变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 49 == tp:  # 5 局部与自变量复合的幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 50 == tp:  # 5 局部与自变量复合的幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sin(np.sqrt(np.abs(x)))
                Y = np.cos(np.sqrt(np.abs(y)))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 51 == tp:  # 5 整体、局部与自变量复合的幂函数变换
        for i in range(1, Q):
            coslist[i] = np.power(np.cos(2 * pi * i / q), 2)
            sinlist[i] = np.power(np.sin(2 * pi * i / q), 2)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.sqrt(np.abs(x))
                Y = np.sqrt(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.cos(X * coslist[i] + Y * sinlist[i]), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 52 == tp:  # 5 整体指数函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 53 == tp:  # 5 整体指数函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 54 == tp:  # 5 局部指数函数变换一
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 55 == tp:  # 5 局部指数函数变换二
        for i in range(1, Q):
            coslist[i] = np.exp(np.sqrt(np.abs(np.cos(2 * pi * i / q))))
            sinlist[i] = np.exp(np.sqrt(np.abs(np.sin(2 * pi * i / q))))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 56 == tp:  # 5 整体与局部复合指数函数变换一
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * coslist[i] + y * sinlist[i]))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 57 == tp:  # 5 整体与局部复合指数函数变换二
        for i in range(1, Q):
            coslist[i] = np.exp(np.cos(2 * pi * i / q))
            sinlist[i] = np.exp(np.sin(2 * pi * i / q))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 58 == tp:  # 5 整体对数函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 59 == tp:  # 5 整体对数函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 60 == tp:  # 5 整体对数函数变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.tan(np.cos(x * coslist[i] + y * sinlist[i]))))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 61 == tp:  # 5 局部对数函数变换
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 62 == tp:  # 5 自变量对数函数变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 63 == tp:  # 5 整体与自变量复合对数函数变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.cos(np.log(np.abs(x)))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 64 == tp:  # 5 整体与局部复合对数函数变换
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 65 == tp:  # 5 局部与自变量复合对数函数变换
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(X * coslist[i] + Y * sinlist[i])
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 66 == tp:  # 5 整体、局部与自变量复合对数函数变换
        for i in range(1, Q):
            coslist[i] = np.log(np.abs(np.cos(2 * pi * i / q)))
            sinlist[i] = np.log(np.abs(np.sin(2 * pi * i / q)))
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                X = np.log(np.abs(x))
                Y = np.log(np.abs(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.log(np.abs(np.cos(X * coslist[i] + Y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 67 == tp:  # 5 叠加三角函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (np.sin(x) + np.cos(y)) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 68 == tp:  # 5 叠加三角函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.cos(np.sin(x) + y) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 69 == tp:  # 5 叠加多项式变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (x + y) / 25
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 70 == tp:  # 5 叠加多项式变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = (x * x + y * y) / 200
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 71 == tp:  # 5 叠加幂函数的变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.cos(temp) + np.power(np.sin(temp), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 72 == tp:  # 5 叠加幂函数的变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    h = h + temp2 + np.power(np.sin(temp), 2) + np.power(temp2, 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 73 == tp:  # 5 叠加幂函数的变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.tan(temp) + np.power(np.cos(temp), 2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 74 == tp:  # 5 叠加幂函数的变换四
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    h = h + temp2 + np.power(temp2, 100) + np.power(temp2, 101)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 75 == tp:  # 5 叠加幂函数的变换五
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.cos(temp)
                    for t in range(1, 6):
                        h = h + np.power(temp2, t)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 76 == tp:  # 5 叠加幂函数的变换六
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    temp2 = np.sin(temp)
                    for t in range(1, 6):
                        h = h + np.abs(temp2)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 77 == tp:  # 5 叠加指数函数的变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.exp(np.cos(x) + np.sin(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 78 == tp:  # 5 叠加对数函数的变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.log(x * x + y * y) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 79 == tp:  # 5 叠加对数函数的变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                add = np.log(np.abs(np.sin(x) + np.cos(y))) / 5
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) + add
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 80 == tp:  # 5 基于绝对值函数变换的叠加幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp)) + np.power(np.sin(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 81 == tp:  # 5 基于绝对值函数变换的叠加幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp) + np.power(np.sin(temp), 2))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 82 == tp:  # 5 基于三角函数变换的叠加幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.cos(np.cos(temp)) + np.power(np.sin(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 83 == tp:  # 5 基于三角函数变换的叠加幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sin(temp) + np.power(np.cos(np.cos(temp)), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 84 == tp:  # 5 基于三角函数变换的叠加幂函数变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.tan(np.sin(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 85 == tp:  # 5 基于指数函数变换的叠加幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.cos(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 86 == tp:  # 5 基于指数函数变换的叠加幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.sin(temp)) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 87 == tp:  # 5 基于对数函数变换的叠加幂函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.cos(temp))) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 88 == tp:  # 5 基于对数函数变换的叠加幂函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 3)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 89 == tp:  # 5 基于对数函数变换的叠加幂函数变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.log(np.abs(np.sin(temp))) + np.power(np.cos(temp), 100)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 90 == tp:  # 5 基于绝对值函数变换的叠加对数函数变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.abs(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 91 == tp:  # 5 基于三角函数变换的叠加对数函数变换
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sin(np.cos(temp)) + np.log(np.abs(np.sin(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 92 == tp:  # 5 基于指数函数变换的叠加对数函数变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.exp(np.cos(temp)) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 93 == tp:  # 5 基于指数函数变换的叠加对数函数变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    temp = x * coslist[i] + y * sinlist[i]
                    h = h + np.sqrt(np.exp(np.sin(temp))) + np.log(np.abs(np.cos(temp)))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 94 == tp:  # 5 三角函数连乘变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.cos(x) * np.cos(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 95 == tp:  # 5 三角函数连乘变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.sin(x) * np.cos(y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 96 == tp:  # 5 三角函数连乘变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.sin(x - y) * np.cos(x + y)
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 97 == tp:  # 5 其他形式连乘变换一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.exp(np.sin(x)) * np.exp(np.cos(y))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 98 == tp:  # 5 其他形式连乘变换二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                p = np.exp(np.sin(x)) * np.exp(np.cos(y)) * np.exp(np.sin(y)) * np.exp(np.cos(x))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 99 == tp:  # 5 其他形式连乘变换三
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                sinx = np.sin(x)
                cosy = np.cos(y)
                p = np.exp(sinx) * np.exp(cosy) * np.log(np.abs(sinx * cosy))
                h = 0
                for i in range(1, Q):
                    h = h + np.cos(x * coslist[i] + y * sinlist[i]) * p
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 100 == tp:  # 5 函数之间自由组合的变换方式一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.cos(x * np.sin(coslist[i]) + y * np.sin(sinlist[i]))) \
                        + np.sqrt(np.abs(np.cos(x * coslist[i] + y * sinlist[i])))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 101 == tp:  # 5 函数之间自由组合的变换方式二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.power(np.tan(np.sin(x * coslist[i] + y * sinlist[i]) *
                                            np.power(np.sin(y * sinlist[i] + x * coslist[i]), 3)), 4)
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 102 == tp:  # 5 函数与变系数的函数变换组合一
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), q))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    elif 103 == tp:  # 5 函数与变系数的函数变换组合二
        for i in range(1, Q):
            coslist[i] = np.cos(2 * pi * i / q)
            sinlist[i] = np.sin(2 * pi * i / q)
        for nx in range(W):
            for ny in range(W):
                x = xmin + (nx - halfw) * deltax
                y = ymin + (ny - halfw) * deltay
                h = 0
                for i in range(1, Q):
                    h = h + np.exp(np.power(np.cos(x * np.cos(coslist[i]) + y * np.sin(sinlist[i])), i))
                h1 = math.ceil(h * mag)
                h_set[ny][nx] = h1
    return h_set


# 对h变换后直接得到k mtd=1
@jit(nopython=True)
def get_k_set(q, s, w, xmin, ymin, tp=0):
    pi = 3.1415927
    Q = round(q) + 1
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
    Q = round(q) + 1
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
