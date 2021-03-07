# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:27:30 2021

@author: EdsonECM17

Define multiple kernel to use in convolutions

"""

import numpy as np

class kernel:
    # Rand 3x3 filter (-0.5, 0-5)
    random = np.random.rand(3,3)-0.5
    # random = [[np.random.rand()-0.5 for i in range(3)] for j in range(3)]
    # Filtro Sharpen Kernel
    sharpen = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), dtype="int")
    # Filtro Laplacian Kernel
    laplacian = np.array(([0, 1, 0],[1, -4, 1],[0, 1, 0]), dtype="int")
    # Filtro sobelX Kernel
    sobelX = np.array(([-1, 0, 1],[-2, 0, 2],[-1, 0, 1]), dtype="int")
    # Filtro sobelY Kernel
    sobelY = np.array(([-1, -2, -1],[0, 0, 0],[1, 2, 1]), dtype="int")
    # Filtro Emboss Kernel
    emboss = np.array(([-2, -1, 0],[-1, 1, 1],[0, 1, 2]), dtype="int")
