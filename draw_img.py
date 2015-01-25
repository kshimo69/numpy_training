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

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.gray)
plt.colorbar()
plt.show()
