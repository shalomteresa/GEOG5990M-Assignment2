
## Site Suitability Analysis Software

PROJECT TITLE: 

Site Suitability Analysis Model

PROJECT DESCRIPTION:

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This model was created for a company that produces rock aggregate in the UK that wants to find suitable sites to locate their factory. 
Three factors — geology, population, and transportation — are used as inputs to the mode and are crucial selection criteria for viable locations. These factors are displayed 
in the model as rasters. 
The programme presents the final output map displaying the acceptable sites and lets the user adjust weights for the factors based on how important they are in evaluating site suitability. 
The user also has the choice of saving the outcome as either a text file or an image.  

Each factor is to be multiplied by a weight and the weighted factors are to be added up to give an overall suitability for each raster location.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DEVELOPMENT PROCESS:

=====================================================================================================================================================================

Reading the data: The input factors were provided as text files containing 2D raster data for each factor with values between [0,255], where higher values indicate
suitability of the site for locating the factory. As the data was in the form of a list of lists read_data function was created to read them as a list of lists
and to display them as rasters in the programme. 

Multiplying weights with the rasters:  A get_weighted_sum function to Calculate the weighted sum of the geology, transport, and population data 
based on the specified weight values defined in the model. 

Rescaling the the rasters: First a get_min_max function was defined to get the minimum and maximum values of the weighted_sum list and a get_rescaled_output
which Rescales the weighted_sum list to values between 0 and 255.

Creating a GUI: GUI was create in order to provide users with a visual and interactive way to interact with the software's functionality.
In order to improve the user experience by providing a more intuitive and user-friendly way to navigate and interact with the software,
buttons to save the results and sliders to set weights were created which make it easier for the users to view results and perform tasks. 
Several functions were created for the purpose of creating GUI like plot function which displays the output image using matplotlib and updates the canvas to plot 
and update function which updates the labels and plot in response to changes in scales. Furthermore, output and image output functions were created to save the 
output as a text file and to save the output image. 

=====================================================================================================================================================================

TESTING:

--------------------------------------------------------------------------------------------------------------------------------------------------

Print statements were used in the initial stages of the development process to check the functionality of the codes in several places. 

Doc test was performed to check the get_weighted_sum function's functionality by importing doctest module.

Unit test was performed for some of the mathematical functions in the model by creating a separate test file and importing the model and unittest.

---------------------------------------------------------------------------------------------------------------------------------------------------

FILE MANIFEST:

============================================================================================================
Software Package Name: MCE
Version: 1.0
Date: May 10, 2023

Files included in this package:

README.md: A text file containing information on the program.
gitignore: A file used by Git to ignore certain files or directories when tracking changes in a repository.
License: A text file containing the software license agreement.
user_manual: A file with instructions for using the software.

Data files:
	data/
		input/ 
			geology.txt
			population.txt
			transport.txt
		output/
			out.txt
			images/
				suitablesite0
			
Source code:
	src/
		MCE/
			test.py
			model.py
			__pycache__
			my_modules/
				io
				__pycache__
				
	.git
		

===============================================================================================================


PREREQUISITES:
------------------------------------------
ANACONDA Distribution Version

Latest version of Spyder

------------------------------------------
USAGE:
=============================

mentioned in the user manual 

=============================

LICENSE:

-----------------------

Apache License 2.0

------------------------

CREDITS:

=======================================================
Andy Turner
https://www.geog.leeds.ac.uk/people/a.turner/index.html

=======================================================

FUTURE DEVELOPMENTS:

-------------------------------------------------------------------------------------------------------------------------------------------------

The sliders in the code are to be set manually so that they add upto 1 , this could be further improved to automate the process where the sliders
automatically get to a default until the weights add upto 1.

There could be a way to input different raster files through the GUI instead of changing the filepaths through the code. 

The final output map could be enhanced to show top 5 sites with different colour hue to make the suitable sites more obvious for display. 


-------------------------------------------------------------------------------------------------------------------------------------------------

BENEFITS:

==========================================================================================================================================================================

Improved decision making: Software for site appropriateness analysis can aid in evaluating and contrasting several site possibilities for a certain project or development.
The software can offer unbiased and quantitative data to enhance decision-making by analysing a variety of elements including ambient conditions, accessibility, 
and infrastructure.

Time and cost savings: Site suitability analysis software can save time and reduce costs associated with manual site assessments and evaluations.
The software can automate the process of analysis, and visualization, providing quick and efficient results.

Increased accuracy and consistency: Site suitability analysis software uses algorithms and models to analyze and evaluate site conditions, 
resulting in more accurate and consistent results compared to manual assessments.

==========================================================================================================================================================================
