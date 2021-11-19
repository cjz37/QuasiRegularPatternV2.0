"""
模型错误
5_5_1_3
6_1_1_2
"""
import cv2 as cv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from lib import colormap as cmp
from lib import mathMoudel as mm
from lib import createImg as ci
from tkinter import messagebox

photo = None
img = None

root = Tk()
root.title('准规则斑图')
root.geometry('1000x600+100+20')
root.resizable(False, False)


class QRP:
    def __init__(self, color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
                 mag=cmp.get_mag(0), tp=0, mtd=0):
        self._color_list = color_list
        self._split_point = split_point
        self._k_list = k_list
        self._mag = mag
        self._tp = tp
        self._mtd = mtd
        self._cImg = None

    def create(self, q, s, w, xmin, ymin):
        # 生成色彩索引
        if 0 == self._mtd:
            color_index = cmp.build_color_index(split_point=self._split_point, k_list=self._k_list, mag=self._mag)
            h_set = mm.get_h_set(q=q, s=s, w=w, xmin=xmin, ymin=ymin, mag=self._mag, tp=self._tp)
            self._cImg = ci.draw_image_h_set(w=w, color_index=color_index, mag=self._mag, color_list=self._color_list,
                                             split_point=self._split_point, h_set=h_set)
        elif 1 == self._mtd:
            k_set = mm.get_k_set(q=q, s=s, w=w, xmin=xmin, ymin=ymin, tp=self._tp)
            self._cImg = ci.draw_image_k_set(w=w, color_list=self._color_list, k_set=k_set)
        elif 2 == self._mtd:
            color_set = mm.get_color_set(q=q, s=s, w=w, xmin=xmin, ymin=ymin, tp=self._tp)
            self._cImg = ci.draw_image_color_set(w=w, color_set=color_set)

    def save(self, name):
        path = 'images/save/' + name + '.png'
        cv.imwrite(path, self._cImg)

    def set_colormap(self, split_point_index, k_list_index, mag_index):
        self._split_point = cmp.get_split_point(split_point_index)
        self._k_list = cmp.get_k_list(k_list_index)
        self._mag = cmp.get_mag(mag_index)


qrp = QRP()


def callback():
    print("~被调用了~")


# 列表框1
def cmb1event(event):
    if "配色方案1" == cmb1.get():
        qrp.set_colormap(0, 0, 0)
    elif "配色方案2" == cmb1.get():
        qrp.set_colormap(0, 1, 0)
    elif "配色方案3" == cmb1.get():
        qrp.set_colormap(1, 2, 1)
    elif "配色方案4" == cmb1.get():
        qrp.set_colormap(2, 3, 1)
    elif "配色方案5" == cmb1.get():
        qrp.set_colormap(0, 4, 0)
    elif "配色方案6" == cmb1.get():
        qrp.set_colormap(4, 5, 1)
    elif "配色方案7" == cmb1.get():
        qrp.set_colormap(5, 6, 0)
    elif "配色方案8" == cmb1.get():
        qrp.set_colormap(6, 7, 0)


# # 列表框2
# def cmb2event(event):
#     if "切割模式1" == cmb1.get():
#         print("1")
#     elif "切割模式2" == cmb1.get():
#         print("2")
#     elif "切割模式3" == cmb1.get():
#         print("3")
#     elif "切割模式..." == cmb1.get():
#         print("more")


def get_value(v=0):
    for key in scales.keys():
        param[key] = scales[key]['value'].get()

    paramVar.set(f"s:{param['s']}, xmin:{param['xmin']}, ymin:{param['ymin']}")


def create():
    # q = param['q']
    q = Eq.get().strip()
    s = param['s']
    w = Ew.get().strip()
    xmin = param['xmin']
    ymin = param['ymin']
    if q and w:
        w = int(w)
        q = float(q)
        if w < 0 or w > 1080:
            tip.config(text='图像大小无效')
        elif q < 0 or q > 28:
            tip.config(text='迭代次数无效')
        else:
            tip.config(text='')
            qrp.create(q=q, s=s, w=w, xmin=xmin, ymin=ymin)

            global photo
            global img
            img = Image.open('images/temp.png')
            size = 600, 600
            img.thumbnail(size)
            photo = ImageTk.PhotoImage(img)
            imgLabel = Label(img_area, image=photo)
            imgLabel.grid(row=0, column=0)
    else:
        tip.config(text='请输入图像大小')


def reset():
    for k, v in scales.items():
        # 初始化滑块
        if 1 == v['pos']:
            v['value'].set(3)
        elif 2 == v['pos']:
            v['value'].set(12)
        elif 3 == v['pos']:
            v['value'].set(1)
        elif 4 == v['pos']:
            v['value'].set(1)
    get_value()
    tip.config(text='')


def save():
    global qrp
    filename = En.get().strip()
    if filename:
        tip.config(text='')
        qrp.save(filename)
        messagebox.showinfo(title='信息提示', message='保存成功！')
    else:
        tip.config(text='请输入文件名')


def chapter2_1():
    chapter_label.config(text='第二章:')
    part_label.config(text='基本图像生成')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=0, mtd=0)
    cmb1.set("配色方案1")


def chapter2_2():
    chapter_label.config(text='第二章:')
    part_label.config(text='两色化处理')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(1),
              mag=cmp.get_mag(0), tp=0, mtd=0)
    cmb1.set("配色方案2")


def chapter3_1():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(1), k_list=cmp.get_k_list(2),
              mag=cmp.get_mag(1), tp=0, mtd=0)
    cmb1.set("配色方案3")


def chapter3_2():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 切割方式二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(2), k_list=cmp.get_k_list(3),
              mag=cmp.get_mag(1), tp=0, mtd=0)
    cmb1.set("配色方案4")


def chapter3_3():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), tp=0, mtd=1)
    cmb1.set("配色方案1")


def chapter3_4():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), tp=1, mtd=1)
    cmb1.set("配色方案1")


def chapter3_5():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(3), k_list=cmp.random_k_list(),
              mag=cmp.get_mag(1), tp=0, mtd=0)
    cmb1.set("配色方案1")


def chapter3_6():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 控制方式一')
    global qrp
    qrp = QRP(tp=0, mtd=2)
    cmb1.set("配色方案1")


def chapter3_7():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 控制方式二')
    global qrp
    qrp = QRP(tp=1, mtd=2)
    cmb1.set("配色方案1")


def chapter3_8():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(1), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(4),
              mag=cmp.get_mag(0), tp=0, mtd=0)
    cmb1.set("配色方案5")


def chapter3_9():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(2), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(4),
              mag=cmp.get_mag(0), tp=0, mtd=0)
    cmb1.set("配色方案5")


def chapter4_1():
    chapter_label.config(text='第四章:')
    part_label.config(text='浮点型q')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(4), k_list=cmp.get_k_list(5),
              mag=cmp.get_mag(1), tp=0, mtd=0)
    cmb1.set("配色方案6")


def chapter4_2():
    chapter_label.config(text='第四章:')
    part_label.config(text='参数i设计一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=1, mtd=0)
    cmb1.set("配色方案1")


def chapter4_3():
    chapter_label.config(text='第四章:')
    part_label.config(text='参数i设计二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=2, mtd=0)
    cmb1.set("配色方案1")


def chapter4_4():
    chapter_label.config(text='第四章:')
    part_label.config(text='参数i设计三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=3, mtd=0)
    cmb1.set("配色方案1")


def chapter4_5():
    chapter_label.config(text='第四章:')
    part_label.config(text='参数i设计四')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=4, mtd=0)
    cmb1.set("配色方案1")


def chapter4_6():
    chapter_label.config(text='第四章:')
    part_label.config(text='其他参数设计一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=5, mtd=0)
    cmb1.set("配色方案1")


def chapter4_7():
    chapter_label.config(text='第四章:')
    part_label.config(text='其他参数设计二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=6, mtd=0)
    cmb1.set("配色方案1")


def chapter4_8():
    chapter_label.config(text='第四章:')
    part_label.config(text='其他参数设计三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=7, mtd=0)
    cmb1.set("配色方案1")


def chapter4_9():
    chapter_label.config(text='第四章:')
    part_label.config(text='其他参数设计四')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=8, mtd=0)
    cmb1.set("配色方案1")


def chapter4_10():
    chapter_label.config(text='第四章:')
    part_label.config(text='其他参数设计五')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=9, mtd=0)
    cmb1.set("配色方案1")


def chapter5_1():
    chapter_label.config(text='第五章:')
    part_label.config(text='绝对值变换')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=10, mtd=0)
    cmb1.set("配色方案1")


def chapter5_2():
    chapter_label.config(text='第五章:')
    part_label.config(text='局部绝对值变换')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=11, mtd=0)
    cmb1.set("配色方案1")


def chapter5_3():
    chapter_label.config(text='第五章:')
    part_label.config(text='复合绝对值变换')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=12, mtd=0)
    cmb1.set("配色方案1")


def chapter5_4():
    chapter_label.config(text='第五章:')
    part_label.config(text='结合参数绝对值')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=13, mtd=0)
    cmb1.set("配色方案1")


def chapter5_5():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=14, mtd=0)
    cmb1.set("配色方案1")


def chapter5_6():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=15, mtd=0)
    cmb1.set("配色方案1")


def chapter5_7():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=16, mtd=0)
    cmb1.set("配色方案1")


def chapter5_8():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换四')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=17, mtd=0)
    cmb1.set("配色方案1")


def chapter5_9():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换五')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=18, mtd=0)
    cmb1.set("配色方案1")


def chapter5_10():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换六')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=19, mtd=0)
    cmb1.set("配色方案1")


def chapter5_11():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换七')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=20, mtd=0)
    cmb1.set("配色方案1")


def chapter5_12():
    chapter_label.config(text='第五章:')
    part_label.config(text='整体三角变换八')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=21, mtd=0)
    cmb1.set("配色方案1")


def chapter5_13():
    chapter_label.config(text='第五章:')
    part_label.config(text='局部三角变换一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=22, mtd=0)
    cmb1.set("配色方案1")


def chapter5_14():
    chapter_label.config(text='第五章:')
    part_label.config(text='局部三角变换二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=23, mtd=0)
    cmb1.set("配色方案1")


def chapter5_15():
    chapter_label.config(text='第五章:')
    part_label.config(text='局部三角变换三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=24, mtd=0)
    cmb1.set("配色方案1")


def chapter5_16():
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量三角变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=25, mtd=0)
    cmb1.set("配色方案1")


def chapter5_17():
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量三角变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=26, mtd=0)
    cmb1.set("配色方案1")


def chapter5_18():  # 整体局部三角变换1
    chapter_label.config(text='第五章:')
    part_label.config(text='复合三角变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=27, mtd=0)
    cmb1.set("配色方案1")


def chapter5_19():  # 整体局部三角变换2
    chapter_label.config(text='第五章:')
    part_label.config(text='复合三角变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=28, mtd=0)
    cmb1.set("配色方案1")


def chapter5_20():  # 整体自变量三角变换1
    chapter_label.config(text='第五章:')
    part_label.config(text='复合三角变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=29, mtd=0)
    cmb1.set("配色方案1")


def chapter5_21():  # 整体自变量三角变换2
    chapter_label.config(text='第五章:')
    part_label.config(text='复合三角变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=30, mtd=0)
    cmb1.set("配色方案1")


def chapter5_22():  # 局部自变量三角变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合三角变换5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
              mag=cmp.get_mag(0), tp=31, mtd=0)
    cmb1.set("配色方案1")


def chapter5_23():  # 基本模型整体幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=32, mtd=0)
    cmb1.set("配色方案7")


def chapter5_24():  # 基本模型整体幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=33, mtd=0)
    cmb1.set("配色方案7")


def chapter5_25():  # 基本模型整体幂函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=34, mtd=0)
    cmb1.set("配色方案7")


def chapter5_26():  # 基本模型整体幂函数变换四
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=35, mtd=0)
    cmb1.set("配色方案7")


def chapter5_27():  # 基本模型整体幂函数变换五
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=36, mtd=0)
    cmb1.set("配色方案7")


def chapter5_28():  # 基本模型整体幂函数变换六
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换6')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=37, mtd=0)
    cmb1.set("配色方案7")


def chapter5_29():  # 基本模型整体幂函数变换七
    chapter_label.config(text='第五章:')
    part_label.config(text='整体幂函数变换7')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=38, mtd=0)
    cmb1.set("配色方案7")


def chapter5_30():  # 基本模型局部幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='局部幂函数变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=39, mtd=0)
    cmb1.set("配色方案7")


def chapter5_31():  # 基本模型局部幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='局部幂函数变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=40, mtd=0)
    cmb1.set("配色方案7")


def chapter5_32():  # 基本模型局部幂函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='局部幂函数变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=41, mtd=0)
    cmb1.set("配色方案7")


def chapter5_33():  # 基本模型局部幂函数变换四
    chapter_label.config(text='第五章:')
    part_label.config(text='局部幂函数变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=42, mtd=0)
    cmb1.set("配色方案7")


def chapter5_34():  # 基本模型自变量幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量幂函数1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=43, mtd=0)
    cmb1.set("配色方案7")


def chapter5_35():  # 基本模型自变量幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量幂函数2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=44, mtd=0)
    cmb1.set("配色方案7")


def chapter5_36():  # 基本模型自变量幂函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量幂函数3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=45, mtd=0)
    cmb1.set("配色方案7")


def chapter5_37():  # 基本模型自变量幂函数变换四
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量幂函数4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=46, mtd=0)
    cmb1.set("配色方案7")


def chapter5_38():  # 基本模型整体与局部复合的幂函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合幂函数变化1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=47, mtd=0)
    cmb1.set("配色方案7")


def chapter5_39():  # 基本模型整体与自变量复合的幂函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合幂函数变化2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=48, mtd=0)
    cmb1.set("配色方案7")


def chapter5_40():  # 基本模型局部与自变量复合的幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='复合幂函数变化3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=49, mtd=0)
    cmb1.set("配色方案7")


def chapter5_41():  # 基本模型局部与自变量复合的幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='复合幂函数变化4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=50, mtd=0)
    cmb1.set("配色方案7")


def chapter5_42():  # 基本模型整体、局部与自变量复合的幂函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合幂函数变化5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=51, mtd=0)
    cmb1.set("配色方案7")


def chapter5_43():  # 基本模型整体指数函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='整体指数变化1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=52, mtd=0)
    cmb1.set("配色方案7")


def chapter5_44():  # 基本模型整体指数函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='整体指数变化2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=53, mtd=0)
    cmb1.set("配色方案7")


def chapter5_45():  # 基本模型局部指数函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='局部指数变化1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=54, mtd=0)
    cmb1.set("配色方案7")


def chapter5_46():  # 基本模型局部指数函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='局部指数变化2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=55, mtd=0)
    cmb1.set("配色方案7")


def chapter5_47():  # 基本模型整体与局部指数函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='复合指数变化1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=56, mtd=0)
    cmb1.set("配色方案7")


def chapter5_48():  # 基本模型整体与局部指数函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='复合指数变化2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=57, mtd=0)
    cmb1.set("配色方案7")


def chapter5_49():  # 基本模型整体对数函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='整体对数变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=58, mtd=0)
    cmb1.set("配色方案7")


def chapter5_50():  # 基本模型整体对数函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='整体对数变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=59, mtd=0)
    cmb1.set("配色方案7")


def chapter5_51():  # 基本模型整体对数函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='整体对数变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=60, mtd=0)
    cmb1.set("配色方案7")


def chapter5_52():  # 基本模型局部对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='局部对数变换')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=61, mtd=0)
    cmb1.set("配色方案7")


def chapter5_53():  # 基本模型自变量对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='自变量对数变换')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=62, mtd=0)
    cmb1.set("配色方案7")


def chapter5_54():  # 基本模型整体与自变量复合对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合对数变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=63, mtd=0)
    cmb1.set("配色方案7")


def chapter5_55():  # 基本模型整体与局部复合对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合对数变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=64, mtd=0)
    cmb1.set("配色方案7")


def chapter5_56():  # 基本模型局部与自变量复合对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合对数变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=65, mtd=0)
    cmb1.set("配色方案7")


def chapter5_57():  # 基本模型整体、局部与自变量复合对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='复合对数变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(5), k_list=cmp.get_k_list(6),
              mag=cmp.get_mag(0), tp=66, mtd=0)
    cmb1.set("配色方案7")


def chapter5_58():  # 叠加三角函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加三角变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=67, mtd=0)
    cmb1.set("配色方案8")


def chapter5_59():  # 叠加三角函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加三角变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=68, mtd=0)
    cmb1.set("配色方案8")


def chapter5_60():  # 叠加多项式变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加多项式变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=69, mtd=0)
    cmb1.set("配色方案8")


def chapter5_61():  # 叠加多项式变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加多项式变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=70, mtd=0)
    cmb1.set("配色方案8")


def chapter5_62():  # 叠加幂函数的变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=71, mtd=0)
    cmb1.set("配色方案8")


def chapter5_63():  # 叠加幂函数的变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=72, mtd=0)
    cmb1.set("配色方案8")


def chapter5_64():  # 叠加幂函数的变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=73, mtd=0)
    cmb1.set("配色方案8")


def chapter5_65():  # 叠加幂函数的变换四
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=74, mtd=0)
    cmb1.set("配色方案8")


def chapter5_66():  # 叠加幂函数的变换五
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=75, mtd=0)
    cmb1.set("配色方案8")


def chapter5_67():  # 叠加幂函数的变换六
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加幂函数变换6')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=76, mtd=0)
    cmb1.set("配色方案8")


def chapter5_68():  # 叠加指数函数的变换
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加指数函数')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=77, mtd=0)
    cmb1.set("配色方案8")


def chapter5_69():  # 叠加对数函数的变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加对数函数1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=78, mtd=0)
    cmb1.set("配色方案8")


def chapter5_70():  # 叠加对数函数的变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='叠加对数函数2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=79, mtd=0)
    cmb1.set("配色方案8")


def chapter5_71():  # 基于绝对值函数变换的叠加幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=80, mtd=0)
    cmb1.set("配色方案8")


def chapter5_72():  # 基于绝对值函数变换的叠加幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=81, mtd=0)
    cmb1.set("配色方案8")


def chapter5_73():  # 基于三角函数变换的叠加幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=82, mtd=0)
    cmb1.set("配色方案8")


def chapter5_74():  # 基于三角函数变换的叠加幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=83, mtd=0)
    cmb1.set("配色方案8")


def chapter5_75():  # 基于三角函数变换的叠加幂函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=84, mtd=0)
    cmb1.set("配色方案8")


def chapter5_76():  # 基于指数函数变换的叠加幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加6')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=85, mtd=0)
    cmb1.set("配色方案8")


def chapter5_77():  # 基于指数函数变换的叠加幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加7')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=86, mtd=0)
    cmb1.set("配色方案8")


def chapter5_78():  # 基于对数函数变换的叠加幂函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加8')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=87, mtd=0)
    cmb1.set("配色方案8")


def chapter5_79():  # 基于对数函数变换的叠加幂函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数与叠加9')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=88, mtd=0)
    cmb1.set("配色方案8")


def chapter5_80():  # 基于对数函数变换的叠加幂函数变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数叠加10')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=89, mtd=0)
    cmb1.set("配色方案8")


def chapter5_81():  # 基于绝对值函数变换的叠加对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数叠加11')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=90, mtd=0)
    cmb1.set("配色方案8")


def chapter5_82():  # 基于三角函数变换的叠加对数函数变换
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数叠加12')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=91, mtd=0)
    cmb1.set("配色方案8")


def chapter5_83():  # 基于指数函数变换的叠加对数函数变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数叠加13')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=92, mtd=0)
    cmb1.set("配色方案8")


def chapter5_84():  # 基于指数函数变换的叠加对数函数变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='基本函数叠加14')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=93, mtd=0)
    cmb1.set("配色方案8")


def chapter5_85():  # 三角函数的连乘变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='三角连乘变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=94, mtd=0)
    cmb1.set("配色方案8")


def chapter5_86():  # 三角函数的连乘变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='三角连乘变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=95, mtd=0)
    cmb1.set("配色方案8")


def chapter5_87():  # 三角函数的连乘变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='三角连乘变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=96, mtd=0)
    cmb1.set("配色方案8")


def chapter5_88():  # 其他形式连乘变换一
    chapter_label.config(text='第五章:')
    part_label.config(text='其他连乘变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=97, mtd=0)
    cmb1.set("配色方案8")


def chapter5_89():  # 其他形式连乘变换二
    chapter_label.config(text='第五章:')
    part_label.config(text='其他连乘变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=98, mtd=0)
    cmb1.set("配色方案8")


def chapter5_90():  # 其他形式连乘变换三
    chapter_label.config(text='第五章:')
    part_label.config(text='其他连乘变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=99, mtd=0)
    cmb1.set("配色方案8")


def chapter5_91():  # 函数之间自由组合的变换方式一
    chapter_label.config(text='第五章:')
    part_label.config(text='自由组合1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=100, mtd=0)
    cmb1.set("配色方案8")


def chapter5_92():  # 函数之间自由组合的变换方式二
    chapter_label.config(text='第五章:')
    part_label.config(text='自由组合2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=101, mtd=0)
    cmb1.set("配色方案8")


def chapter5_93():  # 函数与变系数的函数变换组合一
    chapter_label.config(text='第五章:')
    part_label.config(text='自由组合3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=102, mtd=0)
    cmb1.set("配色方案8")


def chapter5_94():  # 函数与变系数的函数变换组合二
    chapter_label.config(text='第五章:')
    part_label.config(text='自由组合4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=103, mtd=0)
    cmb1.set("配色方案8")


def chapter6_1():  # 求导变换一
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=104, mtd=0)
    cmb1.set("配色方案8")


def chapter6_2():  # 求导变换二
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=105, mtd=0)
    cmb1.set("配色方案8")


def chapter6_3():  # 求导变换三
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=106, mtd=0)
    cmb1.set("配色方案8")


def chapter6_4():  # 求导变换四
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=107, mtd=0)
    cmb1.set("配色方案8")


def chapter6_5():  # 求导变换五
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换5')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=108, mtd=0)
    cmb1.set("配色方案8")


def chapter6_6():  # 求导变换六
    chapter_label.config(text='第六章:')
    part_label.config(text='求导变换6')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=109, mtd=0)
    cmb1.set("配色方案8")


def chapter6_7():  # 基本模型局部的泰勒级数展开式一
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=110, mtd=0)
    cmb1.set("配色方案8")


def chapter6_8():  # 基本模型局部的泰勒级数展开式二
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=111, mtd=0)
    cmb1.set("配色方案8")


def chapter6_9():  # 基本模型局部的泰勒级数展开式三
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开3')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=112, mtd=0)
    cmb1.set("配色方案8")


def chapter6_10():  # 基本模型局部的泰勒级数展开式四
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开4')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=113, mtd=0)
    cmb1.set("配色方案8")


def chapter6_11():  # 基本模型泰勒级数展开式的变换一
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开变换1')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=114, mtd=0)
    cmb1.set("配色方案8")


def chapter6_12():  # 基本模型泰勒级数展开式的变换二
    chapter_label.config(text='第六章:')
    part_label.config(text='泰勒展开变换2')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=115, mtd=0)
    cmb1.set("配色方案8")


def chapter6_13():  # 局部替换的傅里叶展开形式
    chapter_label.config(text='第六章:')
    part_label.config(text='傅里叶展开')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(6), k_list=cmp.get_k_list(7),
              mag=cmp.get_mag(0), tp=116, mtd=0)
    cmb1.set("配色方案8")


# 菜单栏
menubar = Menu(root)
chapter2menu = Menu(menubar, tearoff=False)
chapter2menu.add_command(label="基本图像生成", command=chapter2_1)  # command=?
chapter2menu.add_command(label="两色化处理", command=chapter2_2)
menubar.add_cascade(label="第二章", menu=chapter2menu)

chapter3menu = Menu(menubar, tearoff=False)
chapter3menu.add_command(label="QBColor切割方式一", command=chapter3_1)  # command=?
chapter3menu.add_command(label="QBColor切割方式二", command=chapter3_2)
chapter3menu.add_command(label="QBColor赋值方式一", command=chapter3_3)
chapter3menu.add_command(label="QBColor赋值方式二", command=chapter3_4)
chapter3menu.add_command(label="QBColor赋值方式三", command=chapter3_5)
chapter3menu.add_command(label="RGB等高线变量控制方式一", command=chapter3_6)
chapter3menu.add_command(label="RGB等高线变量控制方式二", command=chapter3_7)
chapter3menu.add_command(label="RGB切割方式一", command=chapter3_8)
chapter3menu.add_command(label="RGB切割方式二", command=chapter3_9)
menubar.add_cascade(label="第三章", menu=chapter3menu)

chapter4menu = Menu(menubar, tearoff=False)
chapter4menu.add_command(label="浮点型q", command=chapter4_1)  # command=?
chapter4menu.add_command(label="参数i的设计一", command=chapter4_2)
chapter4menu.add_command(label="参数i的设计二", command=chapter4_3)
chapter4menu.add_command(label="参数i的设计三", command=chapter4_4)
chapter4menu.add_command(label="参数i的设计四", command=chapter4_5)
chapter4menu.add_command(label="其他参数的设计一", command=chapter4_6)
chapter4menu.add_command(label="其他参数的设计二", command=chapter4_7)
chapter4menu.add_command(label="其他参数的设计三", command=chapter4_8)
chapter4menu.add_command(label="其他参数的设计四", command=chapter4_9)
chapter4menu.add_command(label="其他参数的设计五", command=chapter4_10)
menubar.add_cascade(label="第四章", menu=chapter4menu)

chapter5menu = Menu(menubar, tearoff=False)
chapter5menu.add_command(label="基本模型的绝对值函数变换", command=chapter5_1)  # command=?
chapter5menu.add_command(label="基本模型的局部绝对值函数变换", command=chapter5_2)
chapter5menu.add_command(label="基本模型的复合绝对值函数变换", command=chapter5_3)
chapter5menu.add_command(label="结合参数变化的绝对值函数变化", command=chapter5_4)
chapter5menu.add_command(label="基本模型整体三角变换一", command=chapter5_5)
chapter5menu.add_command(label="基本模型整体三角变换二", command=chapter5_6)
chapter5menu.add_command(label="基本模型整体三角变换三", command=chapter5_7)
chapter5menu.add_command(label="基本模型整体三角变换四", command=chapter5_8)
chapter5menu.add_command(label="基本模型整体三角变换五", command=chapter5_9)
chapter5menu.add_command(label="基本模型整体三角变换六", command=chapter5_10)
chapter5menu.add_command(label="基本模型整体三角变换七", command=chapter5_11)
chapter5menu.add_command(label="基本模型整体三角变换八", command=chapter5_12)
chapter5menu.add_command(label="基本模型局部三角变换一", command=chapter5_13)
chapter5menu.add_command(label="基本模型局部三角变换二", command=chapter5_14)
chapter5menu.add_command(label="基本模型局部三角变换三", command=chapter5_15)
chapter5menu.add_command(label="基本模型自变量三角变换一", command=chapter5_16)
chapter5menu.add_command(label="基本模型自变量三角变换二", command=chapter5_17)
chapter5menu.add_command(label="基本模型整体与局部复合三角变换一", command=chapter5_18)
chapter5menu.add_command(label="基本模型整体与局部复合三角变换二", command=chapter5_19)
chapter5menu.add_command(label="基本模型整体与自变量复合三角变换一", command=chapter5_20)
chapter5menu.add_command(label="基本模型整体与自变量复合三角变换二", command=chapter5_21)
chapter5menu.add_command(label="基本模型局部与自变量复合三角变换", command=chapter5_22)
chapter5menu.add_command(label="基本模型整体幂函数变换一", command=chapter5_23)
chapter5menu.add_command(label="基本模型整体幂函数变换二", command=chapter5_24)
chapter5menu.add_command(label="基本模型整体幂函数变换三", command=chapter5_25)
chapter5menu.add_command(label="基本模型整体幂函数变换四", command=chapter5_26)
chapter5menu.add_command(label="基本模型整体幂函数变换五", command=chapter5_27)
chapter5menu.add_command(label="基本模型整体幂函数变换六", command=chapter5_28)
chapter5menu.add_command(label="基本模型整体幂函数变换七", command=chapter5_29)
chapter5menu.add_command(label="基本模型局部幂函数变换一", command=chapter5_30)
chapter5menu.add_command(label="基本模型局部幂函数变换二", command=chapter5_31)
chapter5menu.add_command(label="基本模型局部幂函数变换三", command=chapter5_32)
chapter5menu.add_command(label="基本模型局部幂函数变换四", command=chapter5_33)
chapter5menu.add_command(label="基本模型自变量幂函数变换一", command=chapter5_34)
chapter5menu.add_command(label="基本模型自变量幂函数变换二", command=chapter5_35)
chapter5menu.add_command(label="基本模型自变量幂函数变换三", command=chapter5_36)
chapter5menu.add_command(label="基本模型自变量幂函数变换四", command=chapter5_37)
chapter5menu.add_command(label="基本模型整体与局部复合幂函数变换", command=chapter5_38)
chapter5menu.add_command(label="基本模型整体与自变量复合幂函数变换", command=chapter5_39)
chapter5menu.add_command(label="基本模型局部与自变量复合幂函数变换一", command=chapter5_40)
chapter5menu.add_command(label="基本模型局部与自变量复合幂函数变换二", command=chapter5_41)
chapter5menu.add_command(label="基本模型整体、局部与自变量复合幂函数变换", command=chapter5_42)
chapter5menu.add_command(label="基本模型整体指数函数变换一", command=chapter5_43)
chapter5menu.add_command(label="基本模型整体指数函数变换二", command=chapter5_44)
chapter5menu.add_command(label="基本模型局部指数函数变换一", command=chapter5_45)
chapter5menu.add_command(label="基本模型局部指数函数变换二", command=chapter5_46)
chapter5menu.add_command(label="基本模型整体与局部复合指数函数变换一", command=chapter5_47)
chapter5menu.add_command(label="基本模型整体与局部复合指数函数变换二", command=chapter5_48)
chapter5menu.add_command(label="基本模型整体对数函数变换一", command=chapter5_49)
chapter5menu.add_command(label="基本模型整体对数函数变换二", command=chapter5_50)
chapter5menu.add_command(label="基本模型整体对数函数变换三", command=chapter5_51)
chapter5menu.add_command(label="基本模型局部对数函数变换", command=chapter5_52)
chapter5menu.add_command(label="基本模型自变量对数函数变换", command=chapter5_53)
chapter5menu.add_command(label="基本模型整体与自变量复合对数函数变换", command=chapter5_54)
chapter5menu.add_command(label="基本模型整体与局部复合对数函数变换", command=chapter5_55)
chapter5menu.add_command(label="基本模型局部与自变量复合对数函数变换", command=chapter5_56)
chapter5menu.add_command(label="基本模型整体、局部与自变量复合对数函数变换", command=chapter5_57)
chapter5menu.add_command(label="叠加三角函数变换一", command=chapter5_58)
chapter5menu.add_command(label="叠加三角函数变换二", command=chapter5_59)
chapter5menu.add_command(label="叠加多项式变换一", command=chapter5_60)
chapter5menu.add_command(label="叠加多项式变换二", command=chapter5_61)
chapter5menu.add_command(label="叠加幂函数变换一", command=chapter5_62)
chapter5menu.add_command(label="叠加幂函数变换二", command=chapter5_63)
chapter5menu.add_command(label="叠加幂函数变换三", command=chapter5_64)
chapter5menu.add_command(label="叠加幂函数变换四", command=chapter5_65)
chapter5menu.add_command(label="叠加幂函数变换五", command=chapter5_66)
chapter5menu.add_command(label="叠加幂函数变换六", command=chapter5_67)
chapter5menu.add_command(label="叠加指数变换", command=chapter5_68)
chapter5menu.add_command(label="叠加对数变换一", command=chapter5_69)
chapter5menu.add_command(label="叠加对数变换二", command=chapter5_70)
chapter5menu.add_command(label="基于绝对值函数变换的叠加幂函数变换一", command=chapter5_71)
chapter5menu.add_command(label="基于绝对值函数变换的叠加幂函数变换二", command=chapter5_72)
chapter5menu.add_command(label="基于三角函数变换的叠加幂函数变换一", command=chapter5_73)
chapter5menu.add_command(label="基于三角函数变换的叠加幂函数变换二", command=chapter5_74)
chapter5menu.add_command(label="基于三角函数变换的叠加幂函数变换三", command=chapter5_75)
chapter5menu.add_command(label="基于指数函数变换的叠加幂函数变换一", command=chapter5_76)
chapter5menu.add_command(label="基于指数函数变换的叠加幂函数变换二", command=chapter5_77)
chapter5menu.add_command(label="基于对数函数变换的叠加幂函数变换一", command=chapter5_78)
chapter5menu.add_command(label="基于对数函数变换的叠加幂函数变换二", command=chapter5_79)
chapter5menu.add_command(label="基于对数函数变换的叠加幂函数变换三", command=chapter5_80)
chapter5menu.add_command(label="基于绝对值函数变换的叠加对数函数变换", command=chapter5_81)
chapter5menu.add_command(label="基于三角函数变换的叠加对数函数变换", command=chapter5_82)
chapter5menu.add_command(label="基于指数函数变换的叠加对数函数变换一", command=chapter5_83)
chapter5menu.add_command(label="基于指数函数变换的叠加对数函数变换二", command=chapter5_84)
chapter5menu.add_command(label="三角函数连乘变换一", command=chapter5_85)
chapter5menu.add_command(label="三角函数连乘变换二", command=chapter5_86)
chapter5menu.add_command(label="三角函数连乘变换三", command=chapter5_87)
chapter5menu.add_command(label="其他形式连乘变换一", command=chapter5_88)
chapter5menu.add_command(label="其他形式连乘变换二", command=chapter5_89)
chapter5menu.add_command(label="其他形式连乘变换三", command=chapter5_90)
chapter5menu.add_command(label="函数之间自由组合的变换方式一", command=chapter5_91)
chapter5menu.add_command(label="函数之间自由组合的变换方式二", command=chapter5_92)
chapter5menu.add_command(label="函数与变系数的函数变换组合一", command=chapter5_93)
chapter5menu.add_command(label="函数与变系数的函数变换组合二", command=chapter5_94)

menubar.add_cascade(label="第五章", menu=chapter5menu)

chapter6menu = Menu(menubar, tearoff=False)
chapter6menu.add_command(label="求导变换一", command=chapter6_1)
chapter6menu.add_command(label="求导变换二", command=chapter6_2)
chapter6menu.add_command(label="求导变换三", command=chapter6_3)
chapter6menu.add_command(label="求导变换四", command=chapter6_4)
chapter6menu.add_command(label="求导变换五", command=chapter6_5)
chapter6menu.add_command(label="求导变换六", command=chapter6_6)
chapter6menu.add_command(label="基本模型局部的泰勒级数展开式一", command=chapter6_7)
chapter6menu.add_command(label="基本模型局部的泰勒级数展开式二", command=chapter6_8)
chapter6menu.add_command(label="基本模型局部的泰勒级数展开式三", command=chapter6_9)
chapter6menu.add_command(label="基本模型局部的泰勒级数展开式四", command=chapter6_10)
chapter6menu.add_command(label="基本模型泰勒级数展开式的变换一", command=chapter6_11)
chapter6menu.add_command(label="基本模型泰勒级数展开式的变换二", command=chapter6_12)
chapter6menu.add_command(label="局部替换的傅里叶展开形式", command=chapter6_13)
menubar.add_cascade(label="第六章", menu=chapter6menu)

root.config(menu=menubar)

frm = Frame(root)
frm.pack()

# 左侧区域
img_area = Frame(frm, width=700, height=600)
qrp_img = PhotoImage(file="images/clear.png")
imgLabel = Label(img_area, image=qrp_img, width=600, height=600)
imgLabel.grid(row=0, column=0)
img_area.pack(side=LEFT)

# 右侧区域
param_area = Frame(frm, width=300, height=600)
chapter_label = Label(param_area, text='第二章:', font=('华文行楷', 20, 'italic'))
chapter_label.grid(row=0, column=0, pady=40)
part_label = Label(param_area, text='基本图像生成', font=('华文行楷', 20, 'italic'), width=15)
part_label.grid(row=0, column=1)

# 滑块
param = {}
v = IntVar()
scales = {  # 'q': {'range': (1, 36), 'value': IntVar(), 'pos': 1, 'describe': "迭代次数"},
    's': {'range': (1, 128), 'value': IntVar(), 'pos': 2, 'describe': "图案密度"},
    # 'w': {'range': (0, 600), 'value': IntVar(), 'pos': 3, 'describe': "图像大小"},
    'xmin': {'range': (-600, 600), 'value': IntVar(), 'pos': 3, 'describe': "中心X坐标偏移"},
    'ymin': {'range': (-600, 600), 'value': IntVar(), 'pos': 4, 'describe': "中心Y坐标偏移"}}
for k, v in scales.items():
    Label(param_area, text=v['describe'], font=('华文行楷', 12)).grid(row=v['pos'], column=0, padx=30)
    scales[k]['target'] = Scale(param_area, variable=v['value'], from_=v['range'][0], to=v['range'][1],
                                orient=HORIZONTAL, length=200, command=get_value)
    scales[k]['target'].grid(row=v['pos'], column=1, columnspan=2)

    # 初始化滑块
    # if 1 == v['pos']:
    #     v['value'].set(3)
    if 2 == v['pos']:
        v['value'].set(12)
    # elif 3 == v['pos']:
    #     v['value'].set(600)
    elif 3 == v['pos']:
        v['value'].set(1)
    elif 4 == v['pos']:
        v['value'].set(1)

Label(param_area, text='迭代次数', font=('华文行楷', 12)).grid(row=1, column=0, pady=15)
Eq = Entry(param_area)
Eq.grid(row=1, column=1)

paramVar = StringVar()
get_value()
# Label(root, text="参数信息:").grid(row=6, column=1, pady=18)
# Label(root, textvariable=paramVar).grid(row=6, column=2)

Label(param_area, text='图像大小', font=('华文行楷', 12)).grid(row=5, column=0, pady=15)
Ew = Entry(param_area)
Ew.grid(row=5, column=1)

# 下拉列表
cmb1 = ttk.Combobox(param_area)
Label(param_area, text="配色方案", font=('华文行楷', 12)).grid(row=7, column=1)
cmb1.grid(row=8, column=1, pady=5)
cmb1['value'] = ('配色方案1', '配色方案2', '配色方案3', '配色方案4', '配色方案5', '配色方案6', '配色方案7', '配色方案8')
cmb1.current(0)

# cmb2 = ttk.Combobox(param_area)
# Label(param_area, text="切割模式:", font=('华文行楷', 12)).grid(row=9, column=1)
# cmb2.grid(row=10, column=1, pady=5)
# cmb2['value'] = ('切割模式1', '切割模式2', '切割模式3', '切割模式...')
# cmb2.current(0)

cmb1.bind("<<ComboboxSelected>>", cmb1event)
# cmb2.bind("<<ComboboxSelected>>", cmb2event)

tip = Label(param_area, font=('华文行楷', 12))
tip.grid(row=7, column=0)

btn1 = Button(param_area, text='生成', font=('华文行楷', 12), width='10', command=create)
btn1.grid(row=8, column=0)

btn2 = Button(param_area, text='保存', font=('华文行楷', 12), width='10', command=save)
btn2.grid(row=9, column=0)

btn3 = Button(param_area, text='重置', font=('华文行楷', 12), width='10', command=reset)
btn3.grid(row=10, column=0)

Label(param_area, text='文件名', font=('华文行楷', 12)).grid(row=9, column=1, pady=0)  # pady=18
En = Entry(param_area)
En.grid(row=10, column=1)

param_area.pack(side=RIGHT)

root.mainloop()
