#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from pylab import *
from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt

# グラフの描画
a = np.arange(20)
plt.plot(a, a**2)       # 線を描画
plt.plot(a, a**2, 'o')  # 線を描画、サンプル点描画
plt.grid()              # グリッドを描画
plt.xlabel('x')         # x軸のラベル
plt.ylabel('y')         # y軸のラベル
# plt.clf()               # 画像の消去 clear figure

# 二次元データを画像に
e = np.eye(3)  # 単位行列
plt.imshow(e)
# plt.imshow(e,interpolation='none')  # 画像をぼやけさせない

# もう少し大きな画像
img = np.random.rand(32, 32)
plt.imshow(img)
plt.gray()  # 色を変える
plt.hot()   # 色を変える

# 複数グラフの同時表示
img = np.random.rand(32, 32)
plt.subplot(131)  # 表示区画を1行3列に設定し、その1番目に描画
plt.imshow(img)

plt.subplot(132)  # 表示区画の2番目を指定
plt.imshow(img)
plt.gray()

plt.subplot(133)  # 表示区画の3番目を指定
plt.imshow(img)
plt.hot()
