# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:22 2023

@author: gy22stp
"""

import my_modules.io as io
from matplotlib import pyplot as plt
import my_modules.geometry as geometry
import os
import imageio


#read the data from txt file

geology = io.data[0]

plt.imshow(geology)
plt.show()


population = io.data[1]

plt.imshow(population)
plt.show()

transport = io.data[2]

plt.imshow(transport)
plt.show()

# Read in the geology, population, and transport rasters
data = io.read_data(['../../data/input/geology.txt', '../../data/input/population.txt', '../../data/input/transport.txt'])
weights = [0.5, 0.3, 0.2]
weighted_rasters = geometry.weighted_rasters(data, weights)
#print(weighted_rasters)

weighted_sum = geometry.add_rasters(weighted_rasters)
#print(weighted_sum)
    
rescaled_raster = geometry.rescale_raster(weighted_sum)
#print(rescaled_raster)

# Create directory to write images to.
try:
    os.makedirs('../../data/output/images/')
except FileExistsError:
    print("path exists")

# For storing images
global ite
ite = 1
images = []

output = io.write_Data(rescaled_raster)


plt.imshow(rescaled_raster, cmap='Blues')
filename = '../../data/output/images/image' + str(ite) + '.png'
plt.savefig(filename)
plt.show()
plt.close()
images.append(imageio.imread(filename))
