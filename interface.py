"""
模型错误
5_5_1_3
6_1_1_2
"""
import cv2 as cv
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
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
            h_set = mm.get_h_set(q=q, s=s, w=w, xmin=xmin, ymin=ymin, mag=self._mag)
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


qrp = QRP()


def callback():
    print("~被调用了~")


# 列表框1
def cmb1event(event):
    if "图案样式1" == cmb1.get():
        print("1")
    elif "图案样式2" == cmb1.get():
        print("2")
    elif "图案样式3" == cmb1.get():
        print("3")
    elif "图案样式..." == cmb1.get():
        print("more")


# 列表框2
def cmb2event(event):
    if "切割模式1" == cmb1.get():
        print("1")
    elif "切割模式2" == cmb1.get():
        print("2")
    elif "切割模式3" == cmb1.get():
        print("3")
    elif "切割模式..." == cmb1.get():
        print("more")


def get_value(v=0):
    for key in scales.keys():
        param[key] = scales[key]['value'].get()

    paramVar.set(f"q:{param['q']}, s:{param['s']}, xmin:{param['xmin']}, ymin:{param['ymin']}")


def create():
    q = param['q']
    s = param['s']
    w = Ew.get().strip()
    xmin = param['xmin']
    ymin = param['ymin']
    if w:
        w = int(w)
        if w < 0 or w > 1080:
            tip.config(text='图像大小无效')
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
            v['value'].set(0)
        elif 4 == v['pos']:
            v['value'].set(0)
    get_value()


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


def chapter2_2():
    chapter_label.config(text='第二章:')
    part_label.config(text='两色化处理')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(1),
              mag=cmp.get_mag(0), tp=0, mtd=0)


def chapter3_1():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(1), k_list=cmp.get_k_list(2),
              mag=cmp.get_mag(1), tp=0, mtd=0)


def chapter3_2():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 切割方式二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(2), k_list=cmp.get_k_list(3),
              mag=cmp.get_mag(1), tp=0, mtd=0)


def chapter3_3():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), tp=0, mtd=1)


def chapter3_4():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式二')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), tp=1, mtd=1)


def chapter3_5():
    chapter_label.config(text='第三章:')
    part_label.config(text='QB 赋值方式三')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(3), k_list=cmp.random_k_list(),
              mag=cmp.get_mag(1), tp=0, mtd=0)


def chapter3_6():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 控制方式一')
    global qrp
    qrp = QRP(tp=0, mtd=2)


def chapter3_7():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 控制方式二')
    global qrp
    qrp = QRP(tp=1, mtd=2)


def chapter3_8():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(1), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(4),
              mag=cmp.get_mag(0), tp=0, mtd=0)


def chapter3_9():
    chapter_label.config(text='第三章:')
    part_label.config(text='RGB 切割方式一')
    global qrp
    qrp = QRP(color_list=cmp.get_color_list(2), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(4),
              mag=cmp.get_mag(0), tp=0, mtd=0)


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
chapter4menu.add_command(label="moudel1", command=callback)  # command=?
chapter4menu.add_command(label="moudel2", command=callback)
chapter4menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第四章", menu=chapter4menu)

chapter5menu = Menu(menubar, tearoff=False)
chapter5menu.add_command(label="moudel1", command=callback)  # command=?
chapter5menu.add_command(label="moudel2", command=callback)
chapter5menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第五章", menu=chapter5menu)

chapter6menu = Menu(menubar, tearoff=False)
chapter6menu.add_command(label="moudel1", command=callback)  # command=?
chapter6menu.add_command(label="moudel2", command=callback)
chapter6menu.add_command(label="moudel...", command=callback)
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
scales = {'q': {'range': (1, 36), 'value': IntVar(), 'pos': 1, 'describe': "迭代次数"},
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
    if 1 == v['pos']:
        v['value'].set(3)
    elif 2 == v['pos']:
        v['value'].set(12)
    # elif 3 == v['pos']:
    #     v['value'].set(600)
    elif 3 == v['pos']:
        v['value'].set(0)
    elif 4 == v['pos']:
        v['value'].set(0)

paramVar = StringVar()
get_value()
# Label(root, text="参数信息:").grid(row=6, column=1, pady=18)
# Label(root, textvariable=paramVar).grid(row=6, column=2)

Label(param_area, text='图像大小', font=('华文行楷', 12)).grid(row=5, column=0, pady=18)
Ew = Entry(param_area)
Ew.grid(row=5, column=1)

# 下拉列表
cmb1 = ttk.Combobox(param_area)
Label(param_area, text="图案样式:", font=('华文行楷', 12)).grid(row=7, column=1)
cmb1.grid(row=8, column=1, pady=5)
cmb1['value'] = ('图案样式1', '图案样式2', '图案样式3', '图案样式...')
cmb1.current(0)

cmb2 = ttk.Combobox(param_area)
Label(param_area, text="切割模式:", font=('华文行楷', 12)).grid(row=9, column=1)
cmb2.grid(row=10, column=1, pady=5)
cmb2['value'] = ('切割模式1', '切割模式2', '切割模式3', '切割模式...')
cmb2.current(0)

cmb1.bind("<<ComboboxSelected>>", cmb1event)
cmb2.bind("<<ComboboxSelected>>", cmb2event)

tip = Label(param_area, font=('华文行楷', 12))
tip.grid(row=7, column=0)

btn1 = Button(param_area, text='生成', font=('华文行楷', 12), width='10', command=create)
btn1.grid(row=8, column=0)

btn2 = Button(param_area, text='保存', font=('华文行楷', 12), width='10', command=save)
btn2.grid(row=9, column=0)

btn3 = Button(param_area, text='重置', font=('华文行楷', 12), width='10', command=reset)
btn3.grid(row=10, column=0)

Label(param_area, text='文件名', font=('华文行楷', 12)).grid(row=11, column=0, pady=18)
En = Entry(param_area)
En.grid(row=11, column=1)

param_area.pack(side=RIGHT)

root.mainloop()
