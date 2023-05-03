# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:22 2023

@author: gy22stp
"""

import my_modules.io as io
import matplotlib
#matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import my_modules.geometry as geometry
import os
import imageio
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def get_weighted_sum(gw, tw, pw, geology, transport, population):
    """
    

    Parameters
    ----------
    gw : TYPE
        DESCRIPTION.
    tw : TYPE
        DESCRIPTION.
    pw : TYPE
        DESCRIPTION.
    geology : TYPE
        DESCRIPTION.
    transport : TYPE
        DESCRIPTION.
    population : TYPE
        DESCRIPTION.

    Returns
    -------
    weighted_sum : TYPE
        DESCRIPTION.

    >>> gw = 0.3
    >>> tw = 0.4
    >>> pw = 0.3
    >>> geology = [[1], [2]]
    >>> transport = [[0], [1]]
    >>> population = [[3], [0]]
    >>> ws = get_weighted_sum(gw, tw, pw, geology, transport, population)
    >>> print(ws)
    [[1.2], [1.0]]
    """
    # Calculate the weighted sum
    weighted_sum = []
    for i in range(len(population)):
        row = []
        for j in range(len(population[0])):
            # Calculate the weighted sum for the current pixel
            row.append(geology[i][j] * gw + population[i][j] * pw + transport[i][j] * tw)
        weighted_sum.append(row)
    return weighted_sum
    
    
    
if __name__ == '__main__' :
    
    # For testing
    import doctest
    doctest.testmod()
    
    #read the data from txt file
        
    geology, n_rows, n_cols = io.read_data('../../data/input/geology.txt')
    
    #print(geology)
    plt.imshow(geology)
    plt.show()
    
    population, n_rows, n_cols = io.read_data('../../data/input/population.txt')
    plt.imshow(population)
    plt.show()
    
    transport, n_rows, n_cols = io.read_data('../../data/input/transport.txt')
    plt.imshow(transport)
    plt.show()
    
    
    # Define the weights
    gw = 0.3
    pw = 0.3
    tw = 0.4
    
    weighted_sum = get_weighted_sum(gw, tw, pw, geology, transport, population)
    # # Calculate the weighted sum
    # weighted_sum = []
    # for i in range(n_rows):
    #     row = []
    #     for j in range(n_cols):
    #         # Calculate the weighted sum for the current pixel
    #         row.append(geology[i][j] * gw + population[i][j] * pw + transport[i][j] * tw)
    #     weighted_sum.append(row)
    
    # Find the maximum and minimum values in combined
    max_val = weighted_sum[0][0]
    min_val = max_val
    for i in range(n_rows):
        for j in range(n_cols):
            max_val = max(max_val, weighted_sum[i][j])
            min_val = min(min_val, weighted_sum[i][j])
            
    print(min_val)
    print(max_val)
    #print(weighted_sum)
    
    # Calculate rescaled output
    rescaled_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            rescaled_value = int((weighted_sum[i][j] - min_val) / (max_val - min_val) * 255)
            #if rescaled_value != 0:
            #    print(rescaled_value)
            # Add the rescaled value to the current row
            row.append(rescaled_value)
        # Add the current row to the output list
        rescaled_output.append(row)
        
    
    # Display the rescaled output as an image
    plt.imshow(rescaled_output)
    plt.show()
    
    
        


   