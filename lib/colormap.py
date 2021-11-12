import numpy as np
import random


def get_mag(index):
    mag = [10, 100]
    return mag[index]


def get_k_list(index):
    k_list = [[2, 10, 8, 5, 6, 13, 15, 6, 10, 11, 6, 12, 6, 12, 15, 14, 6, 10, 1],  # 0
              [1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1],  # 1
              [2, 1, 10, 8, 6, 13, 15, 5, 14, 9, 12, 4, 3, 1, 15, 9, 7, 11, 8, 12, 3, 1, 10, 15, 15, 14, 12, 4, 6, 5,
               13, 10, 2, 1, 14, 8, 12, 15, 6, 7, 15],  # 2
              [11, 14, 12, 5, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 10, 10, 1, 15, 15, 0, 15, 15, 15, 13, 15, 15, 1,
               10, 9],  # 3
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # 4
              ]
    return k_list[index]


def get_split_point(index):
    split_point = [[-9, -5, -4, -3, -2, -1, -0.5, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 1, 2.2, 3, 5, 7, 9, 11],  # 0
                   [-9, -8, -7, -6, -5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.75, -0.5, -0.25, -0.1, 0, 0.1, 0.2, 0.3,
                    0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 11],  # 1
                   [-9, -5, -4, -3, -2, -1.5, -1.45, -1.4, -1.35, -1.3, -1.25, -1.2, -1.15, -1.1, -1.05, -1, -0.95,
                    -0.7, -0.5, -0.2, -0.1, 0, 0.04, 0.2, 0.3, 0.5, 1.5, 3, 5, 7, 9, 11],  # 2
                   [-7.5, -4, -3.5, -1, -2.5, -2, -1.5, -1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.25, 1.5,
                    2, 2.5, 3, 5, 7, 9, 11, 14]  # 3
                   ]
    return split_point[index]


def get_color_list(index):
    QBColor_list = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                    [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192],
                    [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0],
                    [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]
    myColor_list = [[[180, 10, 160], [200, 100, 10], [150, 50, 50], [190, 0, 250],
                    [100, 180, 0], [250, 250, 250], [0, 0, 250], [0, 0, 0],
                    [90, 90, 90], [220, 150, 50], [0, 50, 0], [70, 0, 0],
                    [150, 0, 0], [180, 180, 0], [100, 100, 0], [160, 0, 160],
                    [250, 5, 250], [180, 20, 200], [180, 10, 160]],  # 0
                    [[30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60],
                    [60, 60, 70], [80, 80, 80], [90, 90, 90], [105, 105, 105],
                    [120, 120, 120], [135, 135, 135], [150, 150, 150], [165, 165, 165],
                    [180, 180, 180], [195, 195, 195], [210, 210, 210], [225, 225, 225],
                    [235, 235, 235], [245, 245, 245], [255, 255, 255]]  # 1
                    ]
    if 0 == index:
        return QBColor_list
    else:
        return myColor_list[index-1]


def random_k_list():
    z = int((15 * random.random()) + 1)
    z1 = int((1500 * random.random()) / 100 + 1)
    z2 = int((60 * random.random()) / 4 + 0)
    z3 = int((45 * random.random()) / 3 + 0)
    z4 = int((30 * random.random()) / 2 + 0)
    z5 = int((15 * random.random()) + 0)
    k_list = [z, z1, z2, z1, z3, z, z5 + 1, z2, z5, z5, z1, z4, z1, z1, z2, z4, z, z2, z1, z3, z5, z4, z2, z1, z4, z3,
              z5]
    return k_list


# 建立一个区间的映射
def build_an_interval(a, b, k, mag):
    a = int(a * mag)
    b = int(b * mag)
    seq = np.arange(b, a, -1)
    interval = dict.fromkeys(seq, k)
    return interval


# 建立映射
def build_color_index(split_point, k_list, mag):
    color_index = {}
    for i in range(len(k_list)):
        color_index.update(build_an_interval(split_point[i], split_point[i + 1], k_list[i], mag))
    return color_index
