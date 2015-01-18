#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Shimomura Kimihiko <kshimo69@gmail.com>

import numpy as np


# UnitTest for numpy
np.test()

# version
np.version.version

# search including functions from input keyword
np.lookfor('array')

# create array
a = np.array([1,2,3,4,5])
b = np.array([[1,0,0][0,1,0][0,0,1]])
a
b

a = np.array([1,2,3,4,5], dtype=float)
a
a.dtype

# 0.0から0.1ずつ10.0まで
a = np.arange(0.0,10.0,0.1)
a

