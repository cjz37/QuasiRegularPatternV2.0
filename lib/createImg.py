import numpy as np
import cv2 as cv


# 临时存储，便于显示在界面上
def temp_save(img):
    temp_name = 'temp'
    temp_path = 'images/' + temp_name + '.png'
    cv.imwrite(temp_path, img)


def draw_image_h_set(w, color_index, mag, color_list, split_point, h_set):
    W = w + 1
    # h_set = get_h_set(q, s, w, xmin, ymin, mag, tp)
    color_set = [[color_list[0] for col in range(w + 1)] for row in range(w + 1)]
    if len(color_set) == 0:
        print("No image to draw")
        return
    for i in range(W):
        for j in range(W):
            # color_set[i][j] = color_list[color_index[h_set[i][j]]]
            if h_set[i][j] <= split_point[0] * mag:
                color_set[i][j] = color_list[color_index[split_point[1] * 10]]
            elif h_set[i][j] > split_point[-1] * mag:
                color_set[i][j] = color_list[color_index[split_point[-1] * 10]]
            else:
                color_set[i][j] = color_list[color_index[h_set[i][j]]]
    img = np.array(color_set, dtype=np.uint8)
    temp_save(img)
    return img


def draw_image_k_set(w, color_list, k_set):
    W = w + 1
    # h_set = get_h_set(q, s, w, xmin, ymin, tp)
    color_set = [[color_list[0] for col in range(W)] for row in range(W)]
    if len(color_set) == 0:
        print("No image to draw")
        return
    for i in range(W):
        for j in range(W):
            color_set[i][j] = color_list[k_set[i][j]]
    img = np.array(color_set, dtype=np.uint8)
    temp_save(img)
    return img


def draw_image_color_set(w, color_set):
    W = w + 1
    if len(color_set) == 0:
        print("No points to draw")
        return

    for i in range(W):
        for j in range(W):
            temp = color_set[i][j]
            B = int(temp / 1e6)
            G = int((temp - B * 1e6) / 1e3)
            R = int(temp - B * 1e6 - G * 1e3)
            color_set[i][j] = [B, G, R]

    img = np.array(color_set, dtype=np.uint8)
    temp_save(img)
    return img
