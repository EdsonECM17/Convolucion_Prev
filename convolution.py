# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:07:48 2021

@author: EdsonECM17
"""
import cv2
import numpy as np
# import getpass

from filters import kernel


def normalizar(r,lb,ub):
    return (r-lb)/(ub-lb)

def Convol(image, kernel, stride = 1):
    # Shapes of filter and image
    # image_rows=len(image)
    # image_cols=len(image)
    image_rows, image_cols = image.shape
    # filter_rows=len(kernel)
    # filter_cols=len(kernel[0])
    filter_rows, filter_cols = kernel.shape
    # Shape of output
    total_rows = image_rows - filter_rows + 1
    total_cols = image_cols - filter_cols + 1
    # Initialize output
    conv_output = [[0 for i in range(total_cols)] for j in range(total_rows)]
    conv_output = np.zeros([total_rows, total_cols])
    # Intialize pointers (relatives)
    current_row = 0
    current_col = 0
    # For loop to fill output
    for output_row in range(total_rows):
        for output_col in range(total_cols):
            # Intilize sum value to 0
            s = 0
            # Element wise multiplication (image[zone] * filter)
            # for row in range(filter_rows):
            #     for col in range(filter_cols):
            #         s += kernel[row][col]*image[current_row+row][current_col+col]
            s = np.sum(np.multiply(kernel, 
                                   image[current_row:current_row+filter_rows,
                                         current_col:current_col+filter_cols]))     
            # Save result in output pixel
            conv_output[output_row][output_col]=s
            # Move to next  zone
            current_col = current_col + stride
            # If col analysis is complete, move from row
            if current_col >= total_cols:
                current_col = 0
                current_row = current_row + stride
                # if all rows were analyzed, initialize variable (end loop) 
                if current_row >= total_rows:
                        current_row=0
    return conv_output


def convol_BW(path):
    # Read image
    image = cv2.imread(path, 0)
    # Convol function
    conv_output = Convol(image,kernel.emboss)
    # Show results
    cv2.imwrite('Output_normal.jpg', conv_output)

    # cv2.imshow("Original Image", image)
    # cv2.imshow("Output Image (Emboss)", conv_output)
    # cv2.imshow("Output Uint8", conv_output_uint8)
    # cv2.waitKey(0)
    lb = conv_output.min()
    ub = conv_output.max()
    
    # Normalized results 
    conv_output_normalized = normalizar(conv_output,lb,ub)*255
    cv2.imwrite('Output_normalized.jpg', conv_output_normalized)
    return conv_output, conv_output_normalized
    
def convol_color(path):
    image = cv2.imread(path)
    array_list = []
    array_list_int = []
    for layer in range(0,image.shape[-1]):
        image_layer = image[:,:,layer]
        # Convol function
        conv_output = Convol(image_layer,kernel.emboss)
        # Change output format
        conv_output_uint8 = np.array(conv_output, dtype=np.uint8)
        array_list_int.append(conv_output_uint8)
        array_list.append(conv_output)
    
    layers = len(array_list)
    rows, cols = array_list[0].shape
    conv_output = np.zeros([rows,cols,layers]) 
    conv_output_uint8 = np.zeros([rows,cols,layers]) 
    for i in range(0,layers):
        conv_output_uint8[:,:,i] = array_list_int[i]
        conv_output[:,:,i] = array_list[i]        
    # Show results
    cv2.imshow("Original Image", image)
    cv2.imshow("Output Image (Emboss)", conv_output)
    cv2.imshow("Output Uint8", conv_output_uint8)
    cv2.waitKey(1000)

        


# Read image
image_path = (r'C:\Users\edson\Desktop\Datasets\fashion\img\fashion75.png')
conv_output, conv_output_normalized = convol_BW('Image.jpeg')
    