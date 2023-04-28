# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:56 2023

@author: gy22stp
"""

# Read input data
import csv

def read_data(file_paths):
    # Initialize data list
    data = []

    # Iterate through file paths
    for file_path in file_paths:
        # Initialize list for current file data
        file_data = []
        # Open file and read contents into list
        with open(file_path, newline='') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                file_data.append(row)
        # Append current file data to data list
        data.append(file_data)

    # Return resulting data list
    return data
file_paths = ['../../data/input/geology.txt', '../../data/input/population.txt', '../../data/input/transport.txt']
data = read_data(file_paths)
#print(data)

#print('geology',data[0])

def write_Data(rescaled_raster):
    f = open('../../data/output/out.txt', 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in rescaled_raster:
        writer.writerow(row)
    