# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:22 2023

@author: gy22stp
"""

import my_modules.io as io
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import my_modules.geometry as geometry
import os
import imageio
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import numpy as np
import imageio
import doctest

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
 


def exiting():
    """
    Exit the program.
    """
  
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    
def plot(gw, tw, pw):
    """
    Redraws the canvas

    """
    figure.clear()
   
    weighted_sum = get_weighted_sum(gw, tw, pw, geology, transport, population)
    
    # Find the maximum and minimum values in combined
    max_val = weighted_sum[0][0]
    min_val = max_val
    for i in range(n_rows):
        for j in range(n_cols):
            max_val = max(max_val, weighted_sum[i][j])
            min_val = min(min_val, weighted_sum[i][j])
            
    # print(min_val)
    # print(max_val)
    #print(weighted_sum)
    
    # Calculate rescaled output
    rescaled_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            rescaled_value = int((weighted_sum[i][j] - min_val) / (max_val - min_val) * 255)
            row.append(rescaled_value)
        rescaled_output.append(row)   
    plt.imshow(rescaled_output)
    plt.show()
    canvas.draw()
 
    output(rescaled_output)
        
        
def update(x):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
  
    gw = scale1.get()
    scale1_label.config(text='geology=' + str(round(gw,1)))
    tw = scale2.get()
    scale2_label.config(text='transport=' + str(round(tw,1)))
    pw = scale3.get()
    scale3_label.config(text='population=' + str(round(pw,1)))
    plot(gw, tw, pw)
    
# Initialise figure
figure = plt.figure(figsize=(6, 8))

# Define the weight of each factor and initialise them
gw = 0
tw = 0
pw = 0



def output(output):
    """
    The function to save output files in a given location.
    -------
    
    Writes environment data to a text file and Generates a GIF animation from the images
    saved during the model simulation and saves at the given location.

    Returns
    -------
    None.

    """
    # Write data
    io.write_Data('../../data/output/out.txt', output)
    
    
def image_output():
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")
    
    # For storing images
    global ite
    ite += 1
    images = []
    filename = '../../data/output/images/suitablesite' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
    
    
if __name__ == '__main__' :
    
    # For testing
  
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
    

    
    p0 = None 
    
    # create the GUI
    root = tk.Tk()
    
    # Adding a title
    title = tk.Label(root,text="Multi Criteria Evaluation", font= ('Helvetica', 30), justify = tk.CENTER)
    title.pack(side ='top')
    

    # # create the figure and axes for displaying geology
    # figure1 = plot_geology()
    
    # create the figure and axes for displaying geology
    figure1 = plt.Figure(figsize=(3.5, 3), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.imshow(geology)
    ax1.set_title('Geology')
    cbar = figure1.colorbar(ax1.imshow(geology))
    
    # # create the figure and axes for displaying population
    # figure2 = plot_population()
    
    figure2 = plt.Figure(figsize=(3.5, 3), dpi=100)
    ax2 = figure2.add_subplot(111)
    ax2.imshow(population)
    ax2.set_title('Population')
    cbar = figure2.colorbar(ax2.imshow(population))
    
    # # create the figure and axes for displaying transport
    # figure3 = plot_transport()
    
    # create the figure and axes for displaying transport
    figure3 = plt.Figure(figsize=(3.5, 3), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.imshow(transport)
    ax3.set_title('Transport')
    cbar = figure3.colorbar(ax3.imshow(transport))
    
       
    #Create a frame for the canvas 
    frame_1 = tk.Frame(master=root, padx = 30, pady = -5, bd= 50)
    frame_1.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.CENTER, expand = True)
   
    
    frame_2 = tk.Frame(master=root, padx = 5, pady = 80)
    frame_2.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)
   
    
    frame_3 = tk.Frame(master=root, padx = 30, pady = 80)
    frame_3.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)
   
    
    canvas1 = FigureCanvasTkAgg(figure1, master=frame_1)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=0,column=0)

    
    canvas2 = FigureCanvasTkAgg(figure2, master=frame_1)
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=1,column=0)
    
    
    canvas3 = FigureCanvasTkAgg(figure3, master=frame_1)
    canvas3.draw()
    canvas3.get_tk_widget().grid(row=2,column=0)
    
    
    # Create a canvas to display the figure
    canvas = FigureCanvasTkAgg(figure, master=frame_2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=0)
    
   
   # Create the sliders
    scale1 = ttk.Scale(frame_3, from_=0, to=1, command=update, style="Horizontal.TScale")
    scale1.pack()
    scale1_label = ttk.Label(frame_3, text='Geology')
    scale1.set(gw)
    scale1_label.pack()
    scale2 = ttk.Scale(frame_3, from_=0, to=1, command=update)
    scale2.pack()
    scale2_label = ttk.Label(frame_3, text='Transport')
    scale2.set(pw)
    scale2_label.pack()
    scale3 = ttk.Scale(frame_3, from_=0, to=1, command=update)
    scale3.pack()
    scale3_label = ttk.Label(frame_3, text='Population')
    scale3.set(tw)
    scale3_label.pack()
    
    
    
    # Create a Button widget and link this with the exiting function
    exit_button = ttk.Button(frame_3, text="Exit", command=exiting)
    exit_button.pack(padx = 40, pady =40)
    
    # Create a Button widget and link this with the write function
    write_button = ttk.Button(frame_3, text="Save Result as text",command=output)
    write_button.pack(padx= 40, pady = 40)
    
    # Create a Button widget and link this with the write image function
    write_button = ttk.Button(frame_3, text="Save Result as image",command=image_output)
    write_button.pack(padx = 40, pady = 40)
    
    root.geometry("1300x1000")
    
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    
    root.mainloop()


    
    
        


   