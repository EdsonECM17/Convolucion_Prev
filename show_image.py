# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:12:25 2021

@author: EdsonECM17
"""
import cv2


def show_img(path):
    # Read image pat
    img=cv2.imread(path)
	# Show image
    cv2.imshow("Original Image", img)
    # Schedule a 10 sec delay
    cv2.waitKey(10000)
    # Close window
    cv2.detroyAllWindows()
 # OpenCV uses BGR as its default colour order for images, matplotlib uses RGB.
 # RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)