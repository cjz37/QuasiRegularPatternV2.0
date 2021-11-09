import numpy as np


def get_mag(index):
    mag = [10, 10]
    return mag[index]


def get_k_list(index):
    k_list = [[2, 10, 8, 5, 6, 13, 15, 6, 10, 11, 6, 12, 6, 12, 15, 14, 6, 10, 1],
              [1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1]]
    return k_list[index]


def get_split_point(index):
    split_point = [[-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11],
                   [-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11]]
    return split_point[index]


def get_color_list(index):
    QBColor_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                    [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                    [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                    [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    if 0 == index:
        return QBColor_list
    elif 1 == index:
        return None


def build_an_interval(a, b, k, mag):
    a = int(a * mag)
    b = int(b * mag)
    seq = np.arange(b, a, -1)
    interval = dict.fromkeys(seq, k)
    return interval


def build_color_index(split_point, k_list, mag):
    color_index = {}
    for i in range(len(k_list)):
        color_index.update(build_an_interval(split_point[i], split_point[i+1], k_list[i], mag))
    return color_index
