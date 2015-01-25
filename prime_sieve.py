#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:   Kimihiko Shimomura
# License:  MIT License
# Created:  2015-01-24
#

from pylab import *
from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt

# (100,)のシェイプを持つ真偽値の配列 is_prime を作って True で埋めておく
is_prime = np.ones((100,), dtype=bool)
# 0 と 1 は素数じゃないので除く
is_prime[:2] = False
# 2 から始まる各整数 j を使ってその積になっているものを除く
N_max = int(np.sqrt(len(is_prime)))  # 最大値の平方根の値まで調べればいい
for j in range(2, N_max):
    is_prime[2*j::j] = False

# True のものを取り出す
a = np.transpose(np.nonzero(is_prime))
print a.tolist()
