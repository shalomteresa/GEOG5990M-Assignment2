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

if __name__ == '__main__' :
    #read the data from txt file
    
    geology, n_rows, n_cols = io.read_data('../../data/input/geology.txt')
    
    print(geology)
    plt.imshow(geology)
    plt.show()
    
    population, n_rows, n_cols = io.read_data('../../data/input/population.txt')
    plt.imshow(population)
    plt.show()
    
    transport, n_rows, n_cols = io.read_data('../../data/input/transport.txt')
    plt.imshow(transport)
    plt.show()
    
    
    # Defining the weights 
    gw = 0.3
    pw = 0.3
    tw = 0.4
    
    result = []
    for i in range(n_rows):
        for j in range(n_cols):
            weighted_sum = geology[i][j]*gw + population[i][j]*pw + transport[i][j]*tw 
            result.append(weighted_sum)
            
               
    print(result)
    plt.imshow(result)
    plt.show()
    
    # Rescale the result to be between 0 and 255
    max_val = max(result)
    min_val = min(result)
    scaled_result = [(val - min_val) / (max_val - min_val) * 255 for val in result]

                
    # Reshape the scaled_result list into a 2D array with the same shape as the original data
    scaled_data = np.array(scaled_result).reshape((n_rows, n_cols))
    
    # Display the image
    plt.imshow(scaled_data, cmap='gray')
    plt.show()
    
    
    # # Read in the geology, population, and transport rasters
    # data = io.read_data(['../../data/input/geology.txt', '../../data/input/population.txt', '../../data/input/transport.txt'])
    # weights = [0.3, 0.4, 0.3]
    # weighted_rasters = geometry.weighted_rasters(data, weights)
    # #print(weighted_rasters)
    
    # weighted_sum = geometry.add_rasters(weighted_rasters)
    # #print(weighted_sum)
        
    # rescaled_raster = geometry.rescale_raster(weighted_sum)
    # #print(rescaled_raster)
    
    # # Create directory to write images to.
    # try:
    #     os.makedirs('../../data/output/images/')
    # except FileExistsError:
    #     print("path exists")
    
    # # For storing images
    # global ite
    # ite = 1
    # images = []
    
    # output = io.write_Data(rescaled_raster)

    
    
    # plt.imshow(rescaled_raster)
    # filename = '../../data/output/images/image' + str(ite) + '.png'
    # plt.savefig(filename)
    # plt.show()
    # plt.close()
    # images.append(imageio.imread(filename))

   