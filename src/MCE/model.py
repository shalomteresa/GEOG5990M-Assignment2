# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:08:22 2023

@author: gy22stp
"""

# Modules Imported
import my_modules.io as io
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import os
import imageio
import tkinter as tk
import tkinter.ttk as ttk
import doctest



def get_weighted_sum(gw, tw, pw, geology, transport, population):
    """
    Calculates the weighted sum of the geology, transport, and population data 
    based on the specified weight values.

    Parameters
    ----------
    gw : float
        The weight value for the geology data.
    tw :  float
        The weight value for the transport data.
    pw :float
        The weight value for the population data
    geology :list of lists
        A 2D list of geology data values.
    transport : list of lists
        A 2D list of transport data values.
    population :  list of lists
        A 2D list of population data values.

    Returns
    -------
    weighted_sum : list of lists
        A 2D list of the weighted sum of the input data, with each element 
        corresponding to a pixel in the input data.

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
            row.append(geology[i][j] * gw + population[i][j] * pw + transport[i][j] * tw)
        weighted_sum.append(row)
    return weighted_sum
 
def get_min_max(weighted_sum):
    '''
    Calculates the minimum and maximum values in a 2D list of numbers.

    Parameters
    ----------
    weighted_sum : list
        A 2D list of numbers.

    Returns
    -------
    min_val : tuple
        min_val is the minimum value in weighted_sum.
    max_val : tuple
        max_val is the maximum value in weighted_sum.
        

    '''
    # Get the number of rows and columns in the input 2D list
    n_rows = len(weighted_sum)
    n_cols = len(weighted_sum[0])
    # Initialize max_val and min_val with the first element of the 2D list
    max_val = weighted_sum[0][0]
    min_val = max_val
    # Loop through each element in the 2D list to find the maximum and minimum values
    for i in range(n_rows):
        for j in range(n_cols):
            max_val = max(max_val, weighted_sum[i][j])
            min_val = min(min_val, weighted_sum[i][j])
    # Return a tuple containing the minimum and maximum values found
    return (min_val, max_val)

def get_rescaled_output(weighted_sum):
    '''
    Rescales a matrix of weighted sums to values between 0 and 255.

    Parameters
    ----------
    weighted_sum : list
        A list of lists representing the matrix of weighted sums.

    Returns
    -------
    A list of lists representing the rescaled matrix of values. Each value
        is an integer between 0 and 255.

    '''
    n_rows = len(weighted_sum)
    n_cols = len(weighted_sum[0])
    min_val, max_val = get_min_max(weighted_sum)
    if max_val == min_val:
        # All values are the same, return a constant output
        return [[255 for j in range(n_cols)] for i in range(n_rows)]
    rescaled_output = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            rescaled_value = int((weighted_sum[i][j] - min_val) / (max_val - min_val) * 255)
            row.append(rescaled_value)
        rescaled_output.append(row)
    return rescaled_output

def exiting():
    """
    Exit the program.
 
    """
    root.quit()
    root.destroy()
    
def plot(gw, tw, pw):
    """
   
    The plot function takes in three parameters, gw, tw, and pw, which represent the weights 
    for the geology, transport, and population factors, respectively. 
    It redraws the canvas by calculating the weighted sum of the factors and scaling 
    the output to fit between 0 and 255. The function then displays the output image
    using matplotlib and updates the canvas.
    
    Parameters:
    
    gw (float): weight for the geology factor
    tw (float): weight for the transport factor
    pw (float): weight for the population factor
    
    Returns:
    
    None

    """
    figure.clear()
   
    weighted_sum = get_weighted_sum(gw, tw, pw, geology, transport, population)
    
    min_val, max_val = get_min_max(weighted_sum)
    
    rescaled_output = get_rescaled_output(weighted_sum)
        
    plt.imshow(rescaled_output, cmap = 'Greys')
    plt.title('The darker shades of Grey indicate most suitable sites')
    plt.show()
    canvas.draw()
    
    output(rescaled_output)
        
        
def update(x):
    """
    Updates the labels and plot in response to changes in scales.
    
    Parameters
    ----------
    x : str.
        Number.
        The value of the scale that was changed.

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
ax = figure.add_subplot(111)



# Define the weight of each factor and initialise them
gw = 0
tw = 0
pw = 0



def output(output):
    """
    The function to save output files in a given location.
    -------
    
    Writes the output data to a text file that was generated as the model is run
    and saves at the given location.

    Returns
    -------
    None.

    """
    # Write data
    io.write_Data('../../data/output/out.txt', output)
    
    
def image_output():
    '''
    The function to save output image files in a given location.
    -------
    
    Creates and saves an image of the current plot to a file in the specified directory.
    The image is saved in PNG format and named based on the global variable 'ite'.
    The images are stored in '../../data/output/images/' directory.

    Returns
    -------
    None.

    '''
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")
    
    # For storing images
    global ite
    ite = 0
    images = []
    filename = '../../data/output/images/suitablesite' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
    
    
if __name__ == '__main__' :
    
    # For testing
    doctest.testmod()
    
    
    # Reading and displaying the raster datasets 
    # Read the data from txt file
    geology, n_rows, n_cols = io.read_data('../../data/input/geology.txt')
    # Display the "geology" data using the "imshow" function from the "matplotlib.pyplot" module
    plt.imshow(geology)
    # Display the plot on the screen
    plt.show()
    #print(geology)
    
    # Read the data from txt file
    population, n_rows, n_cols = io.read_data('../../data/input/population.txt')
    # Display the "population" data using the "imshow" function from the "matplotlib.pyplot" module
    plt.imshow(population)
    # Display the plot on the screen
    plt.show()
    #print(population)
    
    # Read the data from txt file
    transport, n_rows, n_cols = io.read_data('../../data/input/transport.txt')
    # Display the "transport" data using the "imshow" function from the "matplotlib.pyplot" module
    plt.imshow(transport)
    # Display the plot on the screen
    plt.show()
    #print(transport)
    
    
    # create the GUI
    root = tk.Tk()
    
    # Adding a title
    title = tk.Label(root,text="Site Suitability Analysis for locating a rock aggregate factory in the UK", font= ('Helvetica', 20), justify = tk.CENTER)
    # Pack the title 
    title.pack(side ='top')
    
    
    # create the figure and axes for displaying geology
    # Create a new figure object called "figure1"
    figure1 = plt.Figure(figsize=(3.5, 3), dpi=100)
    # Create a new subplot within "figure1", and assign it to "ax1". 
    ax1 = figure1.add_subplot(111)
    # Display the "geology" image on the "ax1" subplot using the "imshow" function
    ax1.imshow(geology)
    # Set the title of the "ax1" subplot to "Geology"
    ax1.set_title('Geology')
    # Create a colorbar for the "geology" image, and assign it to "cbar"
    cbar = figure1.colorbar(ax1.imshow(geology))
    # figure1 = plot_geology()
    
 
    # Create a new figure object called "figure2"
    figure2 = plt.Figure(figsize=(3.5, 3), dpi=100)
    # Create a new subplot within "figure2", and assign it to "ax2". 
    ax2 = figure2.add_subplot(111)
    # Display the "population" image on the "ax2" subplot using the "imshow" function
    ax2.imshow(population)
    # Set the title of the "ax2" subplot to "Population"
    ax2.set_title('Population')
    # Create a colorbar for the "population" image, and assign it to "cbar"
    cbar = figure2.colorbar(ax2.imshow(population))
    # figure2 = plot_population()
 
    
    
    # create the figure and axes for displaying transport
    # Create a new figure object called "figure3"
    figure3 = plt.Figure(figsize=(3.5, 3), dpi=100)
    # Create a new subplot within "figure3", and assign it to "ax3". 
    ax3 = figure3.add_subplot(111)
    # Display the "transport" image on the "ax3" subplot using the "imshow" function
    ax3.imshow(transport)
    # Set the title of the "ax3" subplot to "Transport"
    ax3.set_title('Transport')
    # Create a colorbar for the "transport" image, and assign it to "cbar"
    cbar = figure3.colorbar(ax3.imshow(transport))
    # figure3 = plot_transport() 
    
       
    #Create a frame for the canvas 
    # Create a new frame widget called "frame_1" inside the root window
    frame_1 = tk.Frame(master=root, padx = 30, pady = -5, bd= 50)
    # Pack the "frame_1" widget into the left side of the root window
    frame_1.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.CENTER, expand = True)
   
    # Create a new frame widget called "frame_2" inside the root window
    frame_2 = tk.Frame(master=root, padx = 5, pady = 80)
    # Pack the "frame_2" widget into the left side of the root window
    frame_2.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)
   
    # Create a new frame widget called "frame_3" inside the root window
    frame_3 = tk.Frame(master=root, padx = 30, pady = 80)
    # Pack the "frame_3" widget into the left side of the root window
    frame_3.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)
   
    # Create a new Tkinter canvas inside "frame_1" for the "figure1" plot, and assign it to "canvas1"
    canvas1 = FigureCanvasTkAgg(figure1, master=frame_1)
    # Render the plot on the canvas
    canvas1.draw()
    # Get the Tkinter widget associated with "canvas1" and place it in the first row and first column of "frame_1"
    canvas1.get_tk_widget().grid(row=0,column=0)

    # Create a new Tkinter canvas inside "frame_1" for the "figure2" plot, and assign it to "canvas2"
    canvas2 = FigureCanvasTkAgg(figure2, master=frame_1)
    # Render the plot on the canvas
    canvas2.draw()
    # Get the Tkinter widget associated with "canvas2" and place it in the second row and first column of "frame_1"
    canvas2.get_tk_widget().grid(row=1,column=0)
    
    # Create a new Tkinter canvas inside "frame_1" for the "figure3" plot, and assign it to "canvas3"
    canvas3 = FigureCanvasTkAgg(figure3, master=frame_1)
    # Render the plot on the canvas
    canvas3.draw()
    # Get the Tkinter widget associated with "canvas3" and place it in the third row and first column of "frame_1"
    canvas3.get_tk_widget().grid(row=2,column=0)
    
    
    # Create a canvas to display the figure
    # Create a new Tkinter canvas inside "frame_2" for the "figure" plot, and assign it to "canvas"
    canvas = FigureCanvasTkAgg(figure, master=frame_2)
    # Render the plot on the canvas
    canvas.draw()
    # Get the Tkinter widget associated with "canvas" and place it in the first row and first column of "frame_2"
    canvas.get_tk_widget().grid(row=0,column=0)
    
   
    # Create the first slider for setting Geology raster's weight
    scale1 = ttk.Scale(frame_3, from_=0, to=1, command=update, style="Horizontal.TScale")
    scale1.pack()
    # Add label for the slider 
    scale1_label = ttk.Label(frame_3, text='Geology')
    # Set the value of the "scale1" widget to the default value for the "geology" slider
    scale1.set(gw)
    # Pack the "scale1_label" widget
    scale1_label.pack()
    
    # Create the first slider for setting Transport raster's weight
    scale2 = ttk.Scale(frame_3, from_=0, to=1, command=update)
    scale2.pack()
    # Add label for the slider 
    scale2_label = ttk.Label(frame_3, text='Transport')
    # Set the value of the "scale2" widget to the default value for the "transport" slider
    scale2.set(tw)
    # Pack the "scale2_label" widget
    scale2_label.pack()
    
    # Create the first slider for setting Population raster's weight
    scale3 = ttk.Scale(frame_3, from_=0, to=1, command=update)
    scale3.pack()
    # Add label for the slider 
    scale3_label = ttk.Label(frame_3, text='Population')
    # Set the value of the "scale3" widget to the default value for the "population" slider
    scale3.set(pw)
    # Pack the "scale3_label" widget
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
    
    # Set the size of the GUI window
    root.geometry("1300x1100")
    
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    
    
    root.mainloop()


    
    
        


   