import numpy as np
import cv2 as cv


def draw_image(w, color_index, mag, color_list, split_point, h_set):
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
    temp_name = 'temp'
    temp_path = 'images/' + temp_name + '.png'
    cv.imwrite(temp_path, img)
    return img


def draw_image2(w, color_list, h_set):
    W = w + 1
    # h_set = get_h_set(q, s, w, xmin, ymin, tp)
    color_set = [[color_list[0] for col in range(W)] for row in range(W)]
    if len(color_set) == 0:
        print("No image to draw")
        return
    for i in range(W):
        for j in range(W):
            color_set[i][j] = color_list[h_set[i][j]]
    img = np.array(color_set, dtype=np.uint8)
    temp_name = 'temp'
    temp_path = 'images/' + temp_name + '.png'
    cv.imwrite(temp_path, img)
    return img
