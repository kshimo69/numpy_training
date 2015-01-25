#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:   Kimihiko Shimomura
# License:  MIT License
# Created:  2015-01-19
#

from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.plot(x, y, 'o')
plt.show()
