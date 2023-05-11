# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:56 2023

@author: gy22stp
"""

# Modules imported
import csv

# Read input data
def read_data(filepath):
    '''
    Reads input data from a txt file in CSV format

    Parameters
    ----------
    filepath :A list of rows, where each row is a list of values from the CSV file.

    Returns
    -------
    data : A list of rows, where each row is a list of values from the CSV file.
    n_rows : The number of rows in the data.
    n_cols : The number of columns in the data.

    '''
    f = open(filepath, newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    n_rows = len(data)
    print("n_rows", n_rows)
    n_cols0 = len(data[0])
    print("n_cols", n_cols0)
    for row in range(1, n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
    #print(data)
    return data, n_rows, n_cols
    f.close()
    print(data)



def write_Data(filepath,output):
    '''
    Writes output data to a txt file in CSV format.

    Parameters
    ----------
    filepath : string
        The path to the txt file to write.
    output : list of lists
        A list of rows, where each row is a list of values to write to the CSV file.


    Returns
    -------
    None.

    '''
    f = open(filepath, 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in output:
        writer.writerow(row)
    