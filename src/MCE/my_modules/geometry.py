# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:01:52 2023

@author: gy22stp
"""

def weighted_rasters(data, factors):
    """
    Multiplies each raster in the input data list by the corresponding factor in the factors list.

    Args:
        data (list): A list of 2D arrays representing rasters.
        factors (list): A list of numbers representing the factors to multiply each raster with.

    Returns:
        list: A list of 2D arrays representing the multiplied rasters.
    """
    num_rows, num_cols = len(data[2]), len(data[2][0])
    print(num_rows)
    print(num_cols)
    weighted_rasters = []
    for i in range(len(data)):
        raster = data[i]
        factor = factors[i]
        weighted_raster = []
        for row in raster:
            weighted_row = [value * factor for value in row]
            weighted_raster.append(weighted_row)
        weighted_rasters.append(weighted_raster)
    return weighted_rasters

def add_rasters(rasters):
    """
    Adds the input rasters together.

    Args:
        rasters (list): A list of 2D arrays representing rasters.

    Returns:
        list: A 2D array representing the added rasters.
    """
    added_raster = []
    for row_idx in range(len(rasters[0])):
        added_row = []
        for col_idx in range(len(rasters[0][0])):
            pixel_sum = sum(raster[row_idx][col_idx] for raster in rasters)
            added_row.append(pixel_sum)
        added_raster.append(added_row)
    return added_raster

def rescale_raster(raster):
    """
    Rescales the input raster to have values in the range [0, 255].

    Args:
        raster (list): A 2D array representing the raster.

    Returns:
        list: A 2D array representing the rescaled raster.
    """
    min_val = float('inf')
    max_val = float('-inf')
    for row in raster:
        for val in row:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val

    rescaled_raster = []
    for row in raster:
        rescaled_row = []
        for val in row:
            rescaled_val = (val - min_val) / (max_val - min_val) * 255
            rescaled_row.append(rescaled_val)
        rescaled_raster.append(rescaled_row)

    return rescaled_raster